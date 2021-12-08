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
from tools.models import ToolsModel


class LoginView(View):
    """
    Class displaying and validating a login form
    """

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/panel/')
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
            return redirect('/panel/')
        else:
            return render(request, 'admin_app/login.html', {'form': form})


class LogoutView(View):
    """
    Class log user out and redirects to main page
    """

    def get(self, request):
        logout(request)
        return redirect('/')


class PanelView(View):
    """
    Class display panel view
    visible after successful log in
    """

    def get(self, request):
        return render(request, 'admin_app/main.html')
