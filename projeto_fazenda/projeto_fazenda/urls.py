from app_fazenda import views
from django.urls import path

urlpatterns = [
    # Rota, view responsável, nome de referencia
    path('', views.cadastro, name='cadastro'),
    path('listagemdados/', views.listagem, name='dados_fazenda')
]
