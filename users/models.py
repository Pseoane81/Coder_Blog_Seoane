from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserEditForm(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2"]
        help_text = {k:"" for k in fields}
    
class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatares", null=True, blank=True)