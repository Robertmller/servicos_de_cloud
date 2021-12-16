from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

#API
from rest_framework import viewsets
from .models import Servico, Usuario
from rest_framework import permissions
from .serializers import UsuarioSerializer, ServioSerializer


class UsuarioViewssets(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServicoViewsets(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Servico.objects.all()
    serializer_class = ServioSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


def sobre(request):
    return render(request, 'sobre.html')


def servicos(request):
    return render(request, 'servicos.html')


def login(request):
    return render(request, 'login.html')


def cadastro(request):
    return render(request, 'cadastro.html')


#PaginasNotFound
def error404(request):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/thml; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)






