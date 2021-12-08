from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from admin_app.forms import AddToolForm
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


class AddToolView(FormView):
    """
    Class display a form allowing
    to add a new tool to database.
    """
    template_name = 'admin_app/tool.html'
    form_class = AddToolForm
    success_url = '/tools/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


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
