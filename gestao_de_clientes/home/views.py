from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserModel
from django.views.decorators.http import require_POST

# Create your views here.

def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return render(request, 'home.html')


def cadastrar_usuario(request):
    if request.method == "POST":
        try:
            usuario_username = User.objects.get(username=request.POST['username'])
            if usuario_username:
                return render(request, 'novoCliente.html',
                              {'msg': 'Erro! Já existe um usuário com o mesmo username'})

        except User.DoesNotExist:
            try:
                usuario_email = User.objects.get(email=request.POST['email'])

                if usuario_email:
                    return render(request, 'novoCliente.html',
                                  {'msg': 'Erro! Já existe um usuário com o mesmo email'})
            except User.DoesNotExist:
                nome_usuario = request.POST['username']
                email = request.POST['email']
                senha = request.POST['senha']

                novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
                novoUsuario.save()
                return redirect('home')
    else:
        return render(request, "novoCliente.html")

