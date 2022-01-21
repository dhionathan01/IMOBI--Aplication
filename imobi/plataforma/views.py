from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import  login_required


@login_required(login_url='/auth/logar')
def home(request):
    return HttpResponse('Estou na Home')
