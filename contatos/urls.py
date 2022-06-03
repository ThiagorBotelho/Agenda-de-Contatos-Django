from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # index é a função dentro da view
    # Name serve para nomear essa url e usar dentro do html

    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    # Cria o link para clicar no nome no site e referenciar aqui

    path('busca/', views.busca, name='busca'),
]



