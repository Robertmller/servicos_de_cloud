from django.contrib import admin
from .models import Servico, Usuario


class ServicoAdmin(admin.ModelAdmin):
    list_display = ['titulo']


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nomeCompleto']




admin.site.register(Servico, ServicoAdmin)
admin.site.register(Usuario, UsuarioAdmin)

