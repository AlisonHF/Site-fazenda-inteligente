from django.contrib import admin
from app_fazenda import views
from django.urls import path

# Função responsável por registrar os caminhos do nosso site
urlpatterns = [
    # Rota, view responsável, nome de referencia
    path('admin/', admin.site.urls),
    path('', views.cadastro, name='cadastro'),
    path('listagemdados/', views.listagem, name='dados_fazenda')
]
