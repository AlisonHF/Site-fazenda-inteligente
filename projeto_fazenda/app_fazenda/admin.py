from django.contrib import admin
from .models import Dados, Cultivo

# Registro da página de admin
admin.site.register(Dados)
admin.site.register(Cultivo)