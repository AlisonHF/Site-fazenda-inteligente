from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from .models import Dados, Cultivo
from .form import DadosForm, CultivoForm, UpdateDadosForm
from django.contrib.auth.decorators import login_required


# Classe genérica do django para view de delete nos Dados

class DadosDeleteView(DeleteView):
    model = Dados
    template_name = 'dados/excluir.html'
    success_url = reverse_lazy('listagem_dados')



# Classe genérica do django para view de update nos Dados
class DadosUpdateView(UpdateView):
    model = Dados
    form_class = UpdateDadosForm
    template_name = 'dados/editar.html'
    success_url = reverse_lazy('listagem_dados')



# Classe genérica do django para view de delete nos Cultivos
class CultivoDeleteView(DeleteView):
    model = Cultivo
    template_name = 'dados/excluir.html'
    success_url = reverse_lazy('listar_cultivos')



# Classe genérica do django para view de update nos Cultivos
class CultivoUpdateView(UpdateView):
    model = Cultivo
    form_class = CultivoForm
    template_name = 'dados/editar.html'
    success_url = reverse_lazy('listar_cultivos')



# View cadastro dos dados
@login_required
def cadastro(request):
    print(request.POST)
    # Se a requisição da página for POST
    if request.method == 'POST':
        
        form = DadosForm(request.POST, user=request.user)
        # Formulário válido:
        if form.is_valid():
            form.save()
            return redirect('listagem_dados')
        # Formulário não é válido:
        else:
            print(form.errors)
            return render(request, 'dados/cadastro.html', {'form': form})
    # Se a requisição da página for GET
    else:
        form = DadosForm(user=request.user)
    return render(request, 'dados/cadastro.html', {'form': form})



# View listagem dos dados
@login_required
def listagem(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        form = DadosForm(request.POST)
        # Formulário válido:
        if form.is_valid():
            dados_instance = form.save(commit=False)  # Não salva ainda
            dados_instance.usuario = request.user  # Define o usuário
            dados_instance.save()  # Agora salva
            return redirect('listagem_dados')
        # Formulário não é válido:
        else:
            print(form.errors)  # Verificar quais erros estão presentes
            return render(request, 'dados/cadastro.html', {'form': form})

    # Se a requisição da página for GET
    else:
        form = DadosForm()
    
    # Coloca os dados recebidos em um dicionário
    dados = {
        'dados': Dados.objects.filter(usuario=request.user),  # Filtra pelos dados do usuário
        'form': form
    }

    # Retorna a página listagem, com os dados inseridos com sucesso no banco
    return render(request, 'dados/listagem.html', dados)


# View para a tela de seleção do cultivo para detalhes
@login_required
def selecionar(request):
    cultivos = Cultivo.objects.filter(usuario=request.user)
    return render(request, 'detalhe_cultivo/selecionar.html', {'cultivos': cultivos})


# View para tela de detalhes do cultivo
@login_required
def detalhe(request):
    if request.method == 'POST':
        cultivo_nome = request.POST.get('cultivo')
        print(f"Cultivo selecionado: {cultivo_nome}")  # Verifique o nome do cultivo capturado
        
        # Filtra os cultivos pelo nome e pelo usuário logado
        cultivos = Cultivo.objects.filter(nome=cultivo_nome, usuario=request.user)
        print(f"Cultivos encontrados: {cultivos}")  # Verifique os cultivos retornados

        dados_filtrados = Dados.objects.filter(cultivo=cultivo_nome, usuario=request.user)

    # Obtém o último registro
        try:
            ultimo_registro = dados_filtrados.latest('data')
        except Dados.DoesNotExist:
            ultimo_registro = None
        

        # Coloca os dados do contexto em um dict para renderizar as páginas com as informações do dict
        dados = {
            'cultivos': cultivos,
            'ultimo_registro': ultimo_registro
        }

        # Renderiza a página com os dados dos cultivos
        return render(request, 'detalhe_cultivo/detalhe.html', dados)

    # Caso não houver POST
    else:
        return render(request, 'detalhe_cultivo/detalhe.html')
    
# Home
@login_required
def home(request):
    return render(request, 'inicio/home.html')


# View para cadastrar cultivos
@login_required
def cadastrar_cultivo(request):
    # Se a requisição da página for POST
    if request.method == 'POST':
        form = CultivoForm(request.POST)
         # Formulário válido:
        if form.is_valid():
            cultivo_instance = form.save(commit=False)  # Não salva ainda
            cultivo_instance.usuario = request.user  # Define o usuário antes de salvar
            cultivo_instance.save()  # Agora salva
            return redirect('listar_cultivos')
        # Fomulário não válido:
        else: 
            redirect('cadastrar_cultivo/')
    else:
        form = CultivoForm()
    return render(request, 'cultivo/cadastrar.html', {'form': form})


# View para listar os cultivos
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
