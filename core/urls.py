from django.urls import path, include
from .views import index, contato, sobre, servicos

urlpatterns = [
    path('index', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre, name='sobre'),
    path('servicos', servicos, name='serviços')
]
