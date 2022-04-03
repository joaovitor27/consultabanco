from asyncio.windows_events import NULL
from django.shortcuts import render
# Create your views here.
from django.contrib import messages
import requests as req

# Create your views here.
def home(request):
    template_name = 'base.html'

    search = request.GET.get('search')
    if search=='':
        search = 0
        messages.error(request, 'Digite um Numero!')
        context = {}
    else:    
        bancos = req.get(f'https://api-consulta-banco.herokuapp.com/api/books/{search}')
        if bancos.status_code >= 200 and bancos.status_code <=299:
            bancos_data = bancos.json()
            print(bancos_data)
            cod_compensacao = bancos_data['cod_compensacao']
            nome_instituicao = bancos_data['nome_instituicao']
            context = {
                'cod_compensacao': cod_compensacao,
                'nome_instituicao': nome_instituicao
            }
        else:
            context = {}

    return render(request, template_name, context)
