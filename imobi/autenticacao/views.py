from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            return redirect('/auth/cadastro')
        user = User.objects.filter(username=username)

        if user.exists():
            return redirect('/auth/cadastro')
        try:
            user = User(username=username, email=email, password=senha)

            user.save()
            return redirect('/auth/logar')
        except:
            return redirect('/auth/cadastro')


def logar(request):
    return HttpResponse('Logar')
