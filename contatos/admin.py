from django.contrib import admin
from .models import Categoria, Contato

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome',
                    'telefone', 'email', 'mostrar')    # Mostrar cada categoria.
    list_display_links = ('id', 'nome')     # Colocar para acessar os dados (cria o link) no id e pelo nome.
    # list_filter = ('nome', 'sobrenome')     # Cria uma janela de filtro, usando o nome e sobrenome.
    list_per_page = 10                      # Limita a 10 nomes por página.
    search_fields = ('nome', 'sobrenome')   # Cria uma barra de pesquisa para filtrar por nome e sobrenome.
    list_editable = ('telefone', 'mostrar') # Seleciona os campos que podem ser editados diretamente.

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)

