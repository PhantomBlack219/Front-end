from django import forms
from .models import Owasp,Aindice

#Crear formulario
class OwaspForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Owasp

        #especificar los campos
        fields = [
            'nombre',
            'año',        
            ]

class AindicepForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Aindice

        #especificar los campos
        fields = [
            'Aindice',
            'nombreA',        
            ]
