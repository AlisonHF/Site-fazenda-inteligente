from django.urls import path

from . import views

# Lista responsável por registrar os caminhos do nosso site
urlpatterns = [
    path('register/', views.SignUp.as_view(), name='signup')
]
