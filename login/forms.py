from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import User

PROFILE_CHOICES = [
    (1, 'Profile 1'),
    (2, 'Profile 2'),
    (3, 'Profile 3'),
    (4, 'Profile 4'),
    (5, 'Profile 5'),
    (6, 'Profile 6'),
]

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    profile = forms.ChoiceField(
        choices=PROFILE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': "form-control"})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin','is_customer', 'is_employee', 'first_name', 'last_name', 'cedula')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_admin': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_customer': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'is_employee': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.NumberInput(attrs={'max': 99999999, 'min': 0}),
        }

        def clean_cedula(self):
            cedula = self.cleaned_data.get('cedula')
            if not cedula.isdigit() or len(cedula) > 8:
                raise ValidationError('La cédula debe ser numérica y tener un máximo de 8 dígitos.')
            return cedula

        def clean(self):
            cleaned_data = super().clean()
            is_admin = cleaned_data.get('is_admin')
            is_customer = cleaned_data.get('is_customer')
            is_employee = cleaned_data.get('is_employee')

            if not is_admin and not is_customer and not is_employee:
                raise forms.ValidationError("Debe seleccionar al menos un rol.")

            return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    profile = forms.ChoiceField(
        choices=PROFILE_CHOICES,
        widget=forms.RadioSelect(attrs={'class': "form-control"})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'cedula')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Contraseña Actual",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-3 px-4 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline'}),
    )
    new_password1 = forms.CharField(
        label="Nueva Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-3 px-4 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline'}),
    )
    new_password2 = forms.CharField(
        label="Confirmar Nueva Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'shadow appearance-none border rounded w-full py-3 px-4 text-gray-700 mt-1 leading-tight focus:outline-none focus:shadow-outline'}),
    )