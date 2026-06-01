from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cadastro
from .forms import ClienteForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('cadastro:admin')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


def cadastro_publico(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Cadastro realizado com sucesso!'
            )
            return redirect('cadastro:publico')

    else:
        form = ClienteForm()

    return render(
        request,
        'cadastro_publico.html',
        {'form': form}
    )


@login_required
def cadastro_admin(request):

    if not request.user.is_staff:
        messages.error(request, 'Acesso negado.')
        return redirect('cadastro:login')

    if request.method == 'POST':

        if 'delete' in request.POST:

            cadastro = get_object_or_404(
                Cadastro,
                id=int(request.POST['cliente_id'])
            )

            cadastro.delete()

            return redirect('cadastro:admin')

        elif 'update' in request.POST:

            cadastro = get_object_or_404(
                Cadastro,
                id=int(request.POST['cliente_id'])
            )

            form = ClienteForm(
                request.POST,
                instance=cadastro
            )

            if form.is_valid():
                form.save()
                return redirect('cadastro:admin')

            cadastros = Cadastro.objects.all()

            return render(
                request,
                'admin.html',
                {
                    'cadastros': cadastros,
                    'form': form,
                    'cadastro_editando': cadastro,
                }
            )

        else:

            form = ClienteForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('cadastro:admin')

            cadastros = Cadastro.objects.all()

            return render(
                request,
                'admin.html',
                {
                    'cadastros': cadastros,
                    'form': form,
                    'cadastro_editando': None,
                }
            )

    form = ClienteForm()
    cadastros = Cadastro.objects.all()

    return render(
        request,
        'admin.html',
        {
            'cadastros': cadastros,
            'form': form,
            'cadastro_editando': None,
        }
    )