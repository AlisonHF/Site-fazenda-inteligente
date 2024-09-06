from django.db import models

class Dados(models.Model):
    id = models.AutoField(primary_key=True)
    bloco = models.IntegerField()
    cultura = models.TextField(max_length=255)
    ph = models.TextField(max_length=255)
    umidade = models.TextField(max_length=255)
    textura = models.TextField(max_length=255)
