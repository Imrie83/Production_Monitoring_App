from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView, FormView,
)
from admin_app.forms import LoginForm, EmployeeAddForm
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
    departments available.
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


class EmployeeListView(View):
    """
    Class display a list of all
    employees in the company.
    """

    def get(self, request):
        employee_list = EmployeeModel.objects.all()
        return render(
            request,
            'admin_app/employees/employee_list.html',
            {'employee_list': employee_list}
        )


class EmployeeDetailView(View):
    """
    Class display detailed information about an employee.
    """

    def get(self, request, pk):
        try:
            employee_detail = EmployeeModel.objects.get(id=pk)
            return render(
                request,
                'admin_app/employees/employee_details.html',
                {'employee_detail': employee_detail}
            )
        except KeyError:
            return redirect('/employee_list/')


class EmployeeAddView(PermissionRequiredMixin, FormView):
    permission_required = 'admin_app.add_employeemodel'
    template_name = 'admin_app/employees/employeemodel_form.html'
    form_class = EmployeeAddForm
    success_url = '/employee_list/'

    def form_valid(self, form):
        username=form.cleaned_data['username']
        password = form.cleaned_data['password_1']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['user_email']
        staff = form.cleaned_data['staff']
        new_user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=staff,
        )
        employee_id = form.cleaned_data['employee_id']
        position = form.cleaned_data['position']
        department = form.cleaned_data['department']
        new_employee = EmployeeModel.objects.create(
            user=new_user,
            id_num=employee_id,
            position=position,
        )
        new_employee.section_id.set(department)
        return super().form_valid(form)


class EmployeeEditView(PermissionRequiredMixin, FormView):
    permission_required = 'admin_app.edit_employeemodel'
    template_name = 'admin_app/employees/employeemodel_form.html'
    form_class = EmployeeAddForm
    success_url = '/employee_list/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password_1']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['user_email']
        staff = form.cleaned_data['staff']
        new_user = User.objects.update(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=staff,
        )
        employee_id = form.cleaned_data['employee_id']
        position = form.cleaned_data['position']
        department = form.cleaned_data['department']
        new_employee = EmployeeModel.objects.update(
            user=new_user,
            id_num=employee_id,
            position=position,
        )
        new_employee.section_id = department
        return super().form_valid(form)


class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting an employee from database.
    """
    permission_required = 'admin_app.delete_employeemodel'
    template_name = 'admin_app/employees/employeemodel_confirm_delete.html'
    model = EmployeeModel
    success_url = '/employee_list/'
