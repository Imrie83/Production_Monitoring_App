from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from admin_app.forms import LoginForm
from admin_app.models import (
    MachineModel,
    EmployeeModel,
    DepartmentModel,
)


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
        if form.is_valid():
            log_in = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=log_in, password=password)
            if user:
                login(request, user)
                return redirect('/panel/')

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


class MachineListView(View):
    """
    Class display a list of all
    cnc machines available.
    """
    def get(self, request):
        machine_list = MachineModel.objects.all()
        return render(
            request,
            'admin_app/machines/machine_list.html',
            {'machine_list': machine_list}
        )


class MachineDetailView(View):
    """
    Class display detailed view of
    specific machine.
    """
    def get(self, request, pk):
        try:
            machine_detail = MachineModel.objects.get(id=pk)
            return render(
                request,
                'admin_app/machines/machine_details.html',
                {'machine_detail': machine_detail}
            )
        except KeyError:
            return redirect('/machine_list/')


class MachineAddView(PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new machine to database.
    """
    permission_required = 'admin_app.add_machinemodel'
    template_name = 'admin_app/machines/machinemodel_form.html'
    model = MachineModel
    fields = '__all__'
    success_url = '/machine_list/'


class MachineEditView(PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit machine information.
    """
    permission_required = 'admin_app.edit_machinemodel'
    template_name = 'admin_app/machines/machinemodel_form.html'
    model = MachineModel
    fields = '__all__'
    success_url = '/machine_list/'


class MachineDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a machine info from database.
    """
    permission_required = 'admin_app.delete_machinemodel'
    template_name = 'admin_app/machines/machinemodel_confirm_delete.html'
    model = MachineModel
    success_url = '/machine_list/'


class DepartmentListView(View):
    """
    Class display a list of all
    cnc departments available.
    """
    def get(self, request):
        department_list = DepartmentModel.objects.all()
        return render(
            request,
            'admin_app/departments/department_list.html',
            {'department_list': department_list}
        )


class DepartmentDetailView(View):
    """
    Class display detailed view of
    department.
    """
    def get(self, request, pk):
        try:
            department_detail = DepartmentModel.objects.get(id=pk)
            return render(
                request,
                'admin_app/departments/department_details.html',
                {'department_detail': department_detail}
            )
        except KeyError:
            return redirect('/department_list/')


class DepartmentAddView(PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new department to database.
    """
    permission_required = 'admin_app.add_departmentmodel'
    template_name = 'admin_app/departments/departmentmodel_form.html'
    model = DepartmentModel
    fields = '__all__'
    success_url = '/department_list/'


class DepartmentEditView(PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit department information.
    """
    permission_required = 'admin_app.edit_departmentmodel'
    template_name = 'admin_app/departments/departmentmodel_form.html'
    model = DepartmentModel
    fields = '__all__'
    success_url = '/department_list/'


class DepartmentDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a department info from database.
    """
    permission_required = 'admin_app.delete_departmentmodel'
    template_name = 'admin_app/departments/departmentmodel_confirm_delete.html'
    model = DepartmentModel
    success_url = '/department_list/'
