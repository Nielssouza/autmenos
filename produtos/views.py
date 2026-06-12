from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto, MovimentacaoEstoque
from django.contrib import messages
# Create your views here.

#Criar um produto
def produto_novo(request):
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso!')
            return redirect('produtos:produto_lista')
        
    else:
        form = ProdutoForm()
    return render(
        request,
        'produtos/produto_form.html',
        {'form': form}
    )
        
#Listar os produtos
def produto_lista(request):
    produtos = Produto.objects.all().order_by('codigo')

    total_produtos = produtos.count()
    produtos_ativos = produtos.filter(ativo=True).count()

    estoque_baixo = sum(
        1 for produto in produtos
        if produto.status_estoque == 'Baixo'
    )

    valor_total_estoque = sum(
        int(produto.estoque or 0) * produto.valor_venda
        for produto in produtos
    )
    
    valor_total_estoque_formatado = (
        f'{valor_total_estoque:,.2f}'
        .replace(',', 'X')
        .replace('.', ',')
        .replace('X', '.')
    )
    
    sem_estoque = sum(
        1 for produto in produtos
        if produto.status_estoque == 'Sem Estoque'
    )

    movimentacoes = MovimentacaoEstoque.objects.select_related(
        'produto'
    ).order_by('-criado_em')[:10]
    
    return render(
        request,
        'produtos/produto_lista.html',
        {
            'produtos': produtos,
            'total_produtos': total_produtos,
            'produtos_ativos': produtos_ativos,
            'estoque_baixo': estoque_baixo,
            'valor_total_estoque': valor_total_estoque,
            'valor_total_estoque_formatado': valor_total_estoque_formatado,
            'movimentacoes': movimentacoes,
            'sem_estoque': sem_estoque,
        }
    )
#Editar um produto
def produto_editar(request,pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    form = ProdutoForm(request.POST or None, instance=produto)
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('produtos:produto_lista')
        
    
        
    return render(
        request,
        'produtos/produto_form.html',
        {'form': form}
    )
    
#Deletar um produto
def produto_excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    produto.delete()
    messages.success(request, 'Produto excluído com sucesso!')
    
    return redirect('produtos:produto_lista')

#Movimento de produto
def produto_movimentar(request, pk):
    produto = get_object_or_404(
        Produto,
        pk=pk
    )

    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        quantidade = int(
            request.POST.get('quantidade')
        )

        observacao = request.POST.get(
            'observacao'
        )

        estoque_anterior = int(
            produto.estoque or 0
        )

        if tipo == 'E':
            estoque_atual = estoque_anterior + quantidade
        else:
            estoque_atual = estoque_anterior - quantidade

        produto.estoque = estoque_atual
        produto.save()

        MovimentacaoEstoque.objects.create(
            produto=produto,
            tipo=tipo,
            quantidade=quantidade,
            estoque_anterior=estoque_anterior,
            estoque_atual=estoque_atual,
            observacao=observacao,
            usuario=request.user if request.user.is_authenticated else None
        )

        messages.success(
            request,
            'Movimentação registrada com sucesso!'
        )

        return redirect(
            'produtos:produto_lista'
        )

    return render(
        request,
        'produtos/produto_movimentar.html',
        {
            'produto': produto
        }
    )