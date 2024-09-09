from django import forms
from .models import list

class formulario(forms.ModelForm):
    
    class Meta:
        model = list
        fields = ["Name", "Description", "Deadline", "TimeScale"]
