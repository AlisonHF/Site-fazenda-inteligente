from django.contrib import admin
from app_fazenda import views
from django.urls import path, include



# Lista responsável por registrar os caminhos do nosso site
urlpatterns = [
    # Rota, view responsável, nome de referência
    path('home/', views.home, name='home' ),
    # Caminhos parte cadastro

    path('admin/', admin.site.urls),
    path('', views.cadastro, name='cadastro'),
    path('listagemdados/', views.listagem, name='dados_fazenda'),
    path('excluir/<int:pk>/', views.DadosDeleteView.as_view(), name='excluir_dados'),
    path('editar/<int:pk>/', views.DadosUpdateView.as_view(), name='editar_dados'),

    # Caminhos parte detalhes dos dados 
    path('selecionar/', views.selecionar, name='selecionar'),
    path('detalhe/', views.detalhe, name='detalhe'),
    
    # Caminhos cadastrar cultivo
    path('cadastrar_cultivo/', views.cadastrar_cultivo, name='cadastrar_cultivo'),
    path('listagem_cultivos/', views.listar_cultivos, name='listar_cultivos'),
    path('editar_cultivo/<int:pk>/', views.CultivoUpdateView.as_view(), name='editar_cultivo'),
    path('excluir_cultivo/<int:pk>/', views.CultivoDeleteView.as_view(), name='excluir_cultivo'),

    # Registro usuário
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
