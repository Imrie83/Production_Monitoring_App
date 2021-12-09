from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email, URLValidator
from django.core.exceptions import ValidationError
from tools.models import ToolsModel


class LoginForm(forms.Form):
    """
    Class creates login form to be displayed on main page
    """
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
