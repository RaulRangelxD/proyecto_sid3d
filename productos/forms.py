from django import forms
from django.db.models.base import Model
from . import models


class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # Envolver cada campo en un div
            self.fields[field_name].widget = forms.TextInput(attrs={'class': 'input-form'})

    class Meta:
        model = models.Producto
        fields = ['nombre', 'categoria', 'precio', 'precio_2', 'precio_3', 'descripcion', 'imagen', 'existencias']
        categoria = forms.ModelChoiceField(queryset = models.Categoria.objects.all(), to_field_name='nombre', required=True, widget = forms.Select(attrs={'class': 'border border-gray-300 w-full rounded'}))
        widgets = {
            'nombre': forms.TextInput(attrs={'class': ''}),
            'precio': forms.TextInput(attrs={'class': ''}),
            'precio_2' : forms.TextInput(attrs={'class': ''}),
            'precio_3' : forms.TextInput(attrs={'class': ''}),
            'descripcion': forms.Textarea(attrs={'class': ''}),
            'imagen': forms.ClearableFileInput(attrs={'class': ''}),
            'existencias' : forms.TextInput(attrs={'class': ''}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': ''}),
        }