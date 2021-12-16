# Generated by Django 4.0 on 2021-12-15 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field=150, upload_to='', width_field=150)),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=300, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=10)),
                ('telefone', models.IntegerField()),
                ('enderco', models.CharField(max_length=30)),
                ('cpf', models.IntegerField()),
                ('rg', models.IntegerField()),
            ],
        ),
    ]
