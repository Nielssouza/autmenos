from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente #Importa o model Cliente para usar na view
from .forms import ClienteForm

# Create your views here.

#Criando a função view para listar os clientes
#Aqui é onde vamos buscar os dados do banco de dados e passar para o template
def listar_clientes(request):
    
    clientes = Cliente.objects.all()
    
    contexto = {
        'clientes': clientes
    }
    
    return render(request, 'cadastro/listar_clientes.html', contexto)

#Criando a função view para criar um novo cliente
#Aqui é onde vamos receber os dados do formulário, criar um novo cliente no banco de dados e redirecionar para a lista de clientes
def novo_cliente(request):
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:listar_clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'cadastro/novo_cliente.html', {'form': form})

#Criando a função view para editar um cliente existente
#Aqui é onde vamos buscar o cliente pelo ID, receber os dados do formulário, atualizar o cliente no banco de dados e redirecionar para a lista de clientes
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    contexto = {
        'form': form,
        'cliente': cliente
    }
    
    return render(request, 'cadastro/editar_cliente.html', contexto)
   
#Criando a função view para excluir um cliente existente
#Aqui é onde vamos buscar o cliente pelo ID, excluir o cliente do banco de dados e redirecionar para a lista de clientes
def excluir_cliente(request, id):
    
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        
        cliente.delete()
        
        return redirect('listar_clientes')
    
    contexto = {
        'cliente': cliente
    }
    
    return render(request, 'cadastro/excluir_cliente.html', contexto)