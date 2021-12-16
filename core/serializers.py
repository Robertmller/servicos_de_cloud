from rest_framework import serializers
from .models import Servico, Usuario


class ServioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

