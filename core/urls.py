from django.urls import path, include
from .views import index, contato, sobre, servicos, login, cadastro, ServicoViewsets, UsuarioViewssets

#API
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'serviços', ServicoViewsets)
router.register(r'usuarios', UsuarioViewssets)
#-----------FIM API----------#


urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('sobre', sobre, name='sobre'),
    path('servicos', servicos, name='serviços'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('api/v1', include(router.urls)),

]
