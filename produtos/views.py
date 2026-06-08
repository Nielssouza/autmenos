from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto
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
    produtos = Produto.objects.all().order_by('descricao')
    
    return render(
        request,
        'produtos/produto_lista.html',
        {'produtos': produtos}
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