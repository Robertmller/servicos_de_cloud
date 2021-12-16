from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


def sobre(request):
    return render(request, 'sobre.html')


def servicos(request):
    return render(request, 'servicos.html')


