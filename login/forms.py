from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import User

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
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin','is_customer', 'is_employee')

class CustomUserChangeForm(UserChangeForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'password-input', 'id': 'id_password1'}),
        required=False
    )
    password2 = forms.CharField(
        label="Confirme su contraseña",
        widget=forms.PasswordInput(attrs={'class': 'password-input', 'id': 'id_password2'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user