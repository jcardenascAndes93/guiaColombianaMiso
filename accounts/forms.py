from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    Nombres = forms.CharField(max_length=30, help_text='Your first name.')
    Apellidos = forms.CharField(max_length=30, help_text='Your Last Name')
    Email = forms.EmailField(
        max_length=254, help_text='Required. Input valid email address.')
    Telefono = forms.CharField(
        max_length=15, help_text='Your phone number including area code')

