from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from .models import Dados, Plantio
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


# Classe genérica do django para view de delete
class DadosDeleteView(DeleteView):
    model = Dados
    template_name = 'cadastro/confirmar_exclusao.html'
    success_url = reverse_lazy('dados_fazenda')


# Classe genérica do django para view de update
class DadosUpdateView(UpdateView):
    model = Dados
    form_class = DadosForm
    template_name = 'cadastro/editar_dados.html'
    success_url = reverse_lazy('dados_fazenda')


## TESTE ##

def selecionar(request):
    return render(request, 'detalhes_registro/selecionar.html')

def detalhe(request):
    if request.method == 'POST':
        cultivo = request.POST.get('cultivo')
    
        try:
            ultimo_registro = Dados.objects.filter(cultura=cultivo).latest('data')
        except Dados.DoesNotExist:
            ultimo_registro = None

        dados = {
        'plantios': Plantio.objects.filter(nome = cultivo),
        'ultimo_registro': ultimo_registro
    }
        return render(request, 'detalhes_registro/detalhe.html', dados)

    else:
        return render(request, 'detalhes_registro/detalhe.html')
