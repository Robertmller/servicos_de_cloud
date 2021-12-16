from django.db import models


class Servico(models.Model):
    image = models.ImageField('FotoDoProduto', width_field=150, height_field=150)
    titulo = models.CharField('Titulo', max_length=50, null=False, blank=False)
    descricao = models.TextField('Descrição', max_length=300, null=False, blank=False)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nomeCompleto = models.CharField('Nome Completo', max_length=50, null=False, blank=False, editable=True)
    idade = models.IntegerField('Idade', null=False, blank=False, editable=True)
    email = models.EmailField('E-mail', null=False, blank=False, editable=True)
    senha = models.CharField('Senha', max_length=10, null=False, blank=False, editable=True)
    telefone = models.IntegerField('Celular', null=False, blank=False, editable=True)
    enderco = models.CharField('Endereço', max_length=30, null=False, blank=False, editable=True)
    cpf = models.IntegerField('CPF', null=False, blank=False)
    rg = models.IntegerField('RG', null=False, blank=False)

    def __str__(self):
        return self.nomeCompleto

