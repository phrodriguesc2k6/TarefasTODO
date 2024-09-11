from django import forms
from .models import list

class formulario(forms.ModelForm):
    
    class Meta:
        model = list
        fields = ["Name", "Description", "Deadline", "TimeScale"]

class TarefaForm(forms.ModelForm):  # Nome da classe em CamelCase
    class Meta:
        model = list  # Certifique-se de que o modelo está correto
        fields = ["Name", "Description", "Deadline", "TimeScale"]