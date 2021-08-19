from django import forms
from django.forms import fields

from refugio.apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = [
            'nombre','sexo' ,'edad_aproximada','fecha_rescate','persona',
            'vacuna'
            ]
        
        
        
        widgets = {
            
             'persona': forms.Select(attrs={'class': 'form-control my-4'}),
            'vacuna': forms.CheckboxSelectMultiple(attrs={'class': 'check'})
        }
    