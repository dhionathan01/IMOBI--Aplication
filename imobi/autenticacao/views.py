from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        return HttpResponse(f'{username} {email} {senha}')


def logar(request):
    return HttpResponse('Logar')