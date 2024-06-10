from django import forms
from django.db.models.base import Model
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'categoria', 'precio', 'precio_2', 'precio_3', 'descripcion', 'imagen', 'existencias']
        categoria = forms.ModelChoiceField(queryset = models.Categoria.objects.all(), to_field_name='nombre', required=True, widget = forms.Select(attrs={'class': 'border border-gray-300 w-full rounded'}))
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-form'}),
            'precio': forms.TextInput(attrs={'class': 'input-form'}),
            'precio_2' : forms.TextInput(attrs={'class': 'input-form'}),
            'precio_3' : forms.TextInput(attrs={'class': 'input-form'}),
            'descripcion': forms.Textarea(attrs={'class': 'input-form'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'input-form'}),
            'existencias' : forms.TextInput(attrs={'class': 'input-form'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': ''}),
        }