from django.shortcuts import render, redirect
from .models import Dados
from .form import DadosForm 

# Pagina cadastro
def cadastro(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        # Cria o formulário com o ModelForm
        form = DadosForm(request.POST)
        # Formulário válido
        if form.is_valid():
            form.save()
            return redirect('dados_fazenda')
        # Formulário não é válido
        else:
            print(form.errors)  # Verifica quais erros estão presentes
            # Renderiza a página do formulário com os erros
            return render(request, 'cadastro/cadastro.html', {'form': form})
    # Se a requisição da página for GET
    else:
        form = DadosForm()
    return render(request, 'cadastro/cadastro.html', {'form': form})

# Pagina listagem
def listagem(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        form = DadosForm(request.POST)
        # Formulário válido:
        if form.is_valid():
            form.save()  # Salva os dados após validação
            return redirect('dados_fazenda')
        # Formulário não é válido:
        else:
            print(form.errors)  # Verificar quais erros estão presentes

            # Recarrega a página com os erros de validação, se houver
            return render(request, 'cadastro/cadastro.html', {'form': form})
    # Se a requisição da página for GET
    else:
        form = DadosForm()
    
    # Coloca os dados recebidos em um dicionário
    dados = {
        'dados': Dados.objects.all(),
        'form': form
    }

    # Retorna a página listagem, com os dados inseridos com sucesso no banco
    return render(request, 'cadastro/listagem.html', dados)
