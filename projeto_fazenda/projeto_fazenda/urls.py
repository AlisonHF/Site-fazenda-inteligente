from django.contrib import admin
from app_fazenda import views
from django.urls import path

# Função responsável por registrar os caminhos do nosso site
urlpatterns = [
    # Rota, view responsável, nome de referência
    path('admin/', admin.site.urls),
    path('', views.cadastro, name='cadastro'),
    path('listagemdados/', views.listagem, name='dados_fazenda'),
    path('excluir/<int:pk>/', views.DadosDeleteView.as_view(), name='excluir_dados'),
    path('editar/<int:pk>/', views.DadosUpdateView.as_view(), name='editar_dados'),

    path('detalhe/', views.detalhe, name='detalhe')
]
