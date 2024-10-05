from django.db import models
from django.contrib.auth import get_user_model


# Criação do banco de dados para registrar os dados
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

    def __str__(self):
        return self.cultivo  # Certifique-se de retornar o nome desejado



# Criação do banco de dados para tipos de cultivos
class Cultivo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    umidade_recomendado = models.FloatField()
    ph_recomendado = models.FloatField()
    texto_recomendacao = models.TextField(max_length=1200, null=True)
    # Se um usuário for apagado, apagar todos os dados do usuário também
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome  # Certifique-se de retornar o nome desejado
