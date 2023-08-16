from django import forms
from django.core.exceptions import ValidationError

from sitio.models import Noticia


class FormNoticia(forms.Form):
    titulo = forms.CharField(max_length=5)
    archivada = forms.BooleanField(required=False)
    texto = forms.CharField(max_length=500)

    def clean_texto(self):
        data = self.cleaned_data['texto']

        if "forro" in data.lower():
            raise ValidationError("Lenguaje desubicado")

        return data


class FormNoticiaCopado(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'fecha', 'texto']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }
