from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import (
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from admin_app.forms import LoginForm


class LoginView(View):
    """
    Class displaying and validating a login form
    """
    def get(self, request):
        form = LoginForm()
        return render(request, 'admin_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        form.is_valid()
        log_in = form.cleaned_data['login']
        password = form.cleaned_data['password']
        user = authenticate(username=log_in, password=password)
        if user:
            login(request, user)
            return redirect('/panel/', {'login': 'logged in'})
        else:
            return render(request, 'admin_app/login.html',
                          {'login': 'incorrect login credentials',
                           'form': form})


class PanelView(View):
    def get(self, request):
        return render(request, 'admin_app/main.html')
