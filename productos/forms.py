from django import forms
from django.db.models.base import Model
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'categoria', 'precio', 'precio_2', 'precio_3', 'descripcion', 'imagen', 'existencias']
        categoria = forms.ModelChoiceField(queryset = models.Categoria.objects.all(), to_field_name='nombre', required=True, widget = forms.Select(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}))
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
            'precio': forms.TextInput(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
            'precio_2' : forms.TextInput(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
            'precio_3' : forms.TextInput(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
            'descripcion': forms.Textarea(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
            'existencias' : forms.TextInput(attrs={'class': 'w-full px-5 py-4 text-gray-700 bg-gray-200 rounded mb-3'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input input-bordered input-primary w-full max-w-xs'}),
        }