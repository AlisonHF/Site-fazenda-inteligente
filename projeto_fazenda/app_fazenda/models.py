from django.db import models
from django.contrib.auth import get_user_model


# Criação do nosso banco de dados usado para cadastrar os dados do solo
class Dados(models.Model):
    id = models.AutoField(primary_key=True)
    bloco = models.IntegerField()
    cultivo = models.TextField(max_length=255)
    ph = models.FloatField()
    umidade = models.FloatField()
    textura = models.TextField(max_length=255)
    data = models.DateField(auto_now_add=True)
    # Se um usuário for apagado, apagar todos os dados do usuário também
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class Cultivo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    umidade_recomendado = models.FloatField()
    ph_recomendado = models.FloatField()
    texto_recomendacao = models.TextField(max_length=1200, null=True)
    imagem = models.CharField(max_length=1000, blank=True, null=True)
    # Se um usuário for apagado, apagar todos os dados do usuário também
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
