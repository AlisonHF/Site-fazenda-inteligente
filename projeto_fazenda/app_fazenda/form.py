from django import forms
from .models import Dados, Cultivo

# Classe responsável pela criação do formulário
from django import forms
from .models import Dados, Cultivo

class DadosForm(forms.ModelForm):
    # Variável que seta o campo cultivo com opções do model Cultivo
    cultivo = forms.ModelChoiceField(
        queryset=Cultivo.objects,
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label="Escolha uma opção"
    )

    class Meta:
        model = Dados
        # Campos do formulário
        fields = ['bloco', 'cultivo', 'ph', 'umidade', 'textura']
        widgets = {
            'bloco': forms.NumberInput(attrs={'class': 'form-control'}),
            'ph': forms.NumberInput(attrs={'class': 'form-control'}),
            'umidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'textura': forms.Select(attrs={'class': 'form-select'}, choices=[
                (None, 'Escolha uma opção'),
                ('Arenosa', 'Arenosa'),
                ('Argilosa', 'Argilosa'),
                ('Siltosa', 'Siltosa')
            ])
        }

    # Setando informações de inicialização do formulário, com recolhimento
    # do id_usuario para puxar somente os dados do mesmo.
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(DadosForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['cultivo'].queryset = Cultivo.objects.filter(usuario=user) # type: ignore

    # Verificação
    def clean_ph(self):
        ph = self.cleaned_data.get('ph')
        if ph is None:
            raise forms.ValidationError("O pH é obrigatório.")
        if ph < 0 or ph > 14:
            raise forms.ValidationError("O pH deve estar entre 0 e 14.")
        return ph

    # Verificação
    def clean_umidade(self):
        umidade = self.cleaned_data.get('umidade')
        if umidade is None:
            raise forms.ValidationError("A umidade é obrigatória.")
        if umidade < 0 or umidade > 100:
            raise forms.ValidationError("A umidade deve estar entre 0% e 100%.")
        return umidade

    # Verificação
    def clean(self):
        cleaned_data = super().clean()
        ph = cleaned_data.get('ph')
        umidade = cleaned_data.get('umidade')

        if ph and umidade and ph > 7 and umidade < 20:
            raise forms.ValidationError("Umidade muito baixa com pH alto, verifique os valores")

        return cleaned_data



class CultivoForm(forms.ModelForm):
    class Meta:
        model = Cultivo
        # Campos do formulario
        fields = ['nome', 'umidade_recomendado', 'ph_recomendado', 'texto_recomendacao']

        # Campos do formulário com especificações
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'umidade_recomendado': forms.NumberInput(attrs={'class': 'form-control'}),
            'ph_recomendado': forms.NumberInput(attrs={'class': 'form-control'}),
            'texto_recomendacao': forms.Textarea(attrs={'class': 'form-control'}),
        }



# Formulário para o Update dos dados
class UpdateDadosForm(forms.ModelForm):
    # Variável que seta o campo cultivo com opções do model Cultivo
    class Meta:
        model = Dados
        # Campos do formulário
        fields = ['bloco', 'ph', 'umidade', 'textura']
        widgets = {
            'bloco': forms.NumberInput(attrs={'class': 'form-control'}),
            'ph': forms.NumberInput(attrs={'class': 'form-control'}),
            'umidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'textura': forms.Select(attrs={'class': 'form-select'}, choices=[
                (None, 'Escolha uma opção'),
                ('Arenosa', 'Arenosa'),
                ('Argilosa', 'Argilosa'),
                ('Siltosa', 'Siltosa')
            ])
        }
