from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request): # Mostra os contatos da página inicial
    # contatos = Contato.objects.all()    # Selecionando todos os dados da base de dados
    # contatos = Contato.objects.order_by('-id')  # Ordenando os dados pelo ID, de trás pra frente (por isso o -)
    contatos = Contato.objects.order_by('-id').filter(  # Adicionando um filtro, para mostrar somente tal dado
        mostrar = True
    )

    paginator = Paginator(contatos, 20)  # Show 25 contacts per page
    #paginator
    page = request.GET.get('p') # Pega a pagina atual
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos' : contatos
    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)    # Selecionando o dado 'id' da base de dados

    if not contato.mostrar: # Ao pesquisar o id de um nome marcado como não mostrar, levanta o erro 404
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato' : contato
    })


def busca(request):
    termo = request.GET.get('termo')  # Pega a variável termo

    if termo is None or not termo:

        messages.add_message(
            request,
            messages.ERROR,
            'Campo de pesquisa não pode ficar vazio.'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo),  # | vale como 'ou'
        # Pega o termo e verifica se há um nome que seja igual ou que contenha partes do termo
    )


    paginator = Paginator(contatos, 20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })


