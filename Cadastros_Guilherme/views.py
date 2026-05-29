from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente #Importa o model Cliente para usar na view

# Create your views here.

#Criando a função view para listar os clientes
#Aqui é onde vamos buscar os dados do banco de dados e passar para o template
def listar_clientes(request):
    
    clientes = Cliente.objects.all()
    
    contexto = {
        'clientes': clientes
    }
    
    return render(request, 'clientes/listar_clientes.html', contexto)

#Criando a função view para criar um novo cliente
#Aqui é onde vamos receber os dados do formulário, criar um novo cliente no banco de dados e redirecionar para a lista de clientes
def novo_cliente(request):
    
    if request.method == 'POST':
        
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        endereco = request.POST.get('endereco')
        cpf = request.POST.get('cpf')
        data_de_nascimento = request.POST.get('data_nascimento')
        
        Cliente.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            endereco=endereco,
            data_nascimento=data_de_nascimento,
            cpf=cpf,
        )
        return redirect('listar_clientes')
    
    return render(request, 'clientes/novo_cliente.html')

#Criando a função view para editar um cliente existente
#Aqui é onde vamos buscar o cliente pelo ID, receber os dados do formulário, atualizar o cliente no banco de dados e redirecionar para a lista de clientes
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    
    if request.method == 'POST':
        
        cliente.nome = request.POST.get('nome')
        cliente.telefone = request.POST.get('telefone')
        cliente.email = request.POST.get('email')
        cliente.endereco = request.POST.get('endereco')
        cliente.cpf = request.POST.get('cpf')
        cliente.data_nascimento = request.POST.get('data_nascimento')
        
        cliente.save()
        
        return redirect('listar_clientes')
    
    contexto = {
        'cliente': cliente
    }
    
    return render(request, 'clientes/editar_cliente.html', contexto)
   
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
    
    return render(request, 'clientes/excluir_cliente.html', contexto)