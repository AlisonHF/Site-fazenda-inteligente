from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from .models import Dados, Cultivo
from .form import DadosForm, CultivoForm
from django.contrib.auth.decorators import login_required


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




class CultivoDeleteView(DeleteView):
    model = Cultivo
    template_name = 'cultivo/excluir.html'
    success_url = reverse_lazy('listar_cultivos')




class CultivoUpdateView(UpdateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'cultivo/editar.html'
    success_url = reverse_lazy('listar_cultivos')




# View cadastro
@login_required
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


# View listagem
@login_required
def listagem(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        form = DadosForm(request.POST)
        # Formulário válido:
        if form.is_valid():
            dados_instance = form.save(commit=False)  # Não salva ainda
            dados_instance.usuario = request.user  # Define o usuário antes de salvar
            dados_instance.save()  # Agora salva
            return redirect('dados_fazenda')
        # Formulário não é válido:
        else:
            print(form.errors)  # Verificar quais erros estão presentes
            return render(request, 'cadastro/cadastro.html', {'form': form})

    # Se a requisição da página for GET
    else:
        form = DadosForm()
    
    # Coloca os dados recebidos em um dicionário
    dados = {
        'dados': Dados.objects.filter(usuario=request.user),  # Filtra pelos dados do usuário
        'form': form
    }

    # Retorna a página listagem, com os dados inseridos com sucesso no banco
    return render(request, 'cadastro/listagem.html', dados)

# View para a tela de seleção do cultivo para detalhes
@login_required
def selecionar(request):
    return render(request, 'detalhes_registro/selecionar.html')


# View para tela de detalhes do cultivo
@login_required
def detalhe(request):
    if request.method == 'POST':
        cultivo = request.POST.get('cultivo')
    
        # Procura o ultimo registro conforme o cultivo que o usuario passou
        try:
            ultimo_registro = Dados.objects.filter(cultivo=cultivo).latest('data')
        except Dados.DoesNotExist:
            ultimo_registro = None

        # Coloca os dados do context em um dict para renderizar as paginas com
        # as informações do dict
        dados = {
        'cultivos': Cultivo.objects.filter(nome = cultivo),
        'ultimo_registro': ultimo_registro
    }
        # Caso houver ultimo registro
        return render(request, 'detalhes_registro/detalhe.html', dados)

    # Caso não houver
    else:
        return render(request, 'detalhes_registro/detalhe.html')
@login_required
def home(request):
    return render(request, 'inicio/home.html')

# Parte cultivos

@login_required
def cadastrar_cultivo(request):
    if request.method == 'POST':
        form = CultivoForm(request.POST)
        if form.is_valid():
            cultivo_instance = form.save(commit=False)  # Não salva ainda
            cultivo_instance.usuario = request.user  # Define o usuário antes de salvar
            cultivo_instance.save()  # Agora salva
            return redirect('listar_cultivos')
    else:
        form = CultivoForm()

    return render(request, 'cultivo/cadastrar.html', {'form': form})

@login_required
def listar_cultivos(request):
    # Obtém todos os cultivos cadastrados para o usuário logado
    cultivos = Cultivo.objects.filter(usuario=request.user)  # Filtra pelos cultivos do usuário

    # Cria um dicionário com os cultivos para passar ao template
    dados = {
        'dados': cultivos
    }

    # Retorna a página de listagem, com os cultivos do banco de dados
    return render(request, 'cultivo/listar_cultivos.html', dados)