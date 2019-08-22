from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tourist


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Your first name.')
    last_name = forms.CharField(max_length=30, help_text='Your Last Name')
    email = forms.EmailField(max_length=254, help_text='Required. Input valid email address.')
    phone = forms.CharField(max_length=15, help_text='Your phone number including area code')


