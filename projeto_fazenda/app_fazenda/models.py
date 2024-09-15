from django.db import models


# Criação do nosso banco de dados usado para cadastrar os dados do solo
class Dados(models.Model):
    id = models.AutoField(primary_key=True)
    bloco = models.IntegerField()
    cultura = models.TextField(max_length=255)
    ph = models.FloatField(max_length=255)
    umidade = models.FloatField(max_length=255)
    textura = models.TextField(max_length=255)
    data = models.DateField(auto_now_add=True)
