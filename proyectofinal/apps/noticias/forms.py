from django import forms
from .models import *



class Form_Alta(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ('titulo', 'contenido', 'imagen', 'categoria')
        widgets = {
            'categoria': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
                'type': 'checkbox', 
                'value': '',
                'id':'defaultCheck1',
            })
        }



class Form_Modificacion(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('contenido','imagen','categoria')
        categoria = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        


