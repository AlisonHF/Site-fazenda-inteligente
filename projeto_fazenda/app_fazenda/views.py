from django.shortcuts import render, redirect
from .models import Dados

def cadastro(request): 
    return render(request, 'cadastro/cadastro.html')

def listagem(request):
    # Pegando os dados dos inputs e salvando apenas se for POST
    if request.method == 'POST':
        novos_dados = Dados(
            bloco=request.POST.get('bloco'),
            cultura=request.POST.get('cultura'),
            ph=request.POST.get('ph'),
            umidade=request.POST.get('umidade'),
            textura=request.POST.get('textura')
        )
        novos_dados.save()

        # Redirecionando após o salvamento para evitar o resubmit do formulário
        return redirect('listagem')

    # Se for GET, simplesmente exibe os dados sem salvar
    dados = {
        'dados': Dados.objects.all()
    }

    return render(request, 'cadastro/listagem.html', dados)