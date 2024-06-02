from django import forms
from django.db.models.base import Model
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'categoria', 'precio', 'precio_2', 'precio_3', 'descripcion', 'imagen', 'existencias']
        categoria = forms.ModelChoiceField(queryset = models.Categoria.objects.all(), to_field_name='nombre', required=True, widget = forms.Select(attrs={'class': 'form-control'}))
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'precio_2' : forms.TextInput(attrs={'class': 'form-control'}),
            'precio_3' : forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'existencias' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }