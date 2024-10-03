from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import TextInput, PasswordInput

class CreateUserForm(UserCreationForm):
    class meta:
        model=User
        fields=['First Name','Last Name', 'Username', 'Password','Confirm Password']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())