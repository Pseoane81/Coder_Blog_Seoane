from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","last_name", "password1", "password2"]
        help_text = {k:"" for k in fields}


class UsuarioModelForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username' , 'last_name', 'email')