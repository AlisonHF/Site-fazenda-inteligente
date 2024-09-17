from django import forms
from .models import Dados



# Classe responsável pela criação do formulário
class DadosForm(forms.ModelForm):
    # Classe para especificar o modelo do banco e os campos
    class Meta:
        ESCOLHA_CULTIVOS = [
        (None, 'Escolha uma opção'),
        ('Tomate', 'Tomate'),
        ('Alface', 'Alface'),
        ('Beterraba', 'Beterraba')
    ]
        model = Dados
        fields = ['bloco', 'cultivo', 'ph', 'umidade', 'textura']
        # Colocando estilos nos campos pré-definidos pelo django
        widgets = {
            'bloco': forms.NumberInput(attrs={'class': 'form-control'}),
            'cultivo': forms.Select(attrs={'class': 'form-select'}, choices=ESCOLHA_CULTIVOS),
            'ph': forms.NumberInput(attrs={'class': 'form-control'}),
            'umidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'textura': forms.TextInput(attrs={'class': 'form-control'})
        }
        
    # Validação específica do campo ph
    def clean_ph(self):
        ph = self.cleaned_data.get('ph')
        if ph is None:
            raise forms.ValidationError("O pH é obrigatório.")
        if ph < 0 or ph > 14:
            raise forms.ValidationError("O pH deve estar entre 0 e 14.")
        return ph

    # Validação específica do campo umidade
    def clean_umidade(self):
        umidade = self.cleaned_data.get('umidade')
        if umidade is None:
            raise forms.ValidationError("A umidade é obrigatória.")
        if umidade < 0 or umidade > 100:
            raise forms.ValidationError("A umidade deve estar entre 0% e 100%.")
        return umidade
    
    # Validação geral do formulário
    def clean(self):
        cleaned_data = super().clean()
        ph = cleaned_data.get('ph')
        umidade = cleaned_data.get('umidade')

        # Se os dados coletados em ph e umidade forem discrepantes:
        if ph and umidade and ph > 7 and umidade < 20:
            raise forms.ValidationError("Umidade muito baixa com pH alto, verifique os valores")

        return cleaned_data
