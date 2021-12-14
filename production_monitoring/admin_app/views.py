from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, \
    LoginRequiredMixin
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)
from admin_app.forms import (
    LoginForm,
    EmployeeAddForm,
    EmployeeEditForm,
    DatePicker,
)
from admin_app.models import (
    MachineModel,
    EmployeeModel,
    DepartmentModel,
    UserProductModel,
)
from products.models import ProductsModel, ProductComponent


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


class PanelView(LoginRequiredMixin, View):
    """
    Class display panel view
    visible after successful log in
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        current_employee = EmployeeModel.objects.get(user=request.user)
        user_group = []

        for value in current_employee.user.groups.all():
            user_group.append(value.name)

        now = datetime.now().strftime('%Y-%m-%d')

        if 'Shop floor staff' in user_group:
            my_output = UserProductModel.objects.filter(
                user_id=current_employee,
                prod_end__icontains=now,
            )
        else:
            my_output = ''
        return render(
            request,
            'admin_app/main.html',
            {'output': my_output},
        )


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


class MachineDetailView(LoginRequiredMixin, View):
    """
    Class display detailed view of
    specific machine.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

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


class MachineAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new machine to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'admin_app.add_machinemodel'
    template_name = 'admin_app/machines/machinemodel_form.html'
    model = MachineModel
    fields = '__all__'
    success_url = '/machine_list/'


class MachineEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit machine information.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'admin_app.edit_machinemodel'
    template_name = 'admin_app/machines/machinemodel_form.html'
    model = MachineModel
    fields = '__all__'
    success_url = '/machine_list/'


class MachineDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a machine info from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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


class DepartmentDetailView(LoginRequiredMixin, View):
    """
    Class display detailed view of
    department.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

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


class DepartmentAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new department to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'admin_app.add_departmentmodel'
    template_name = 'admin_app/departments/departmentmodel_form.html'
    model = DepartmentModel
    fields = '__all__'
    success_url = '/department_list/'


class DepartmentEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit department information.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'admin_app.edit_departmentmodel'
    template_name = 'admin_app/departments/departmentmodel_form.html'
    model = DepartmentModel
    fields = '__all__'
    success_url = '/department_list/'


class DepartmentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a department info from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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

    def post(self, request):
        if 'search' in request.POST:
            search_q = request.POST['search']
            employee_list = EmployeeModel.objects.filter(
                Q(id_num__icontains=search_q) |
                Q(position__icontains=search_q) |
                Q(user__first_name__icontains=search_q) |
                Q(user__last_name__icontains=search_q) |
                Q(user__email__icontains=search_q)
            ).order_by('user__username')
            return render(
                request,
                'admin_app/employees/employee_list.html',
                {'employee_list': employee_list}
            )


class EmployeeDetailView(LoginRequiredMixin, View):
    """
    Class display detailed information about an employee.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        try:
            employee_detail = EmployeeModel.objects.get(id=pk)
            employee_list = EmployeeModel.objects.all()
            return render(
                request,
                'admin_app/employees/employee_details.html',
                {
                    'employee_detail': employee_detail,
                    'employee_list': employee_list,
                 }
            )
        except KeyError:
            return redirect('/employee_list/')

    def post(self, request, pk):
        if 'search' in request.POST:
            search_q = request.POST['search']
            employee_list = EmployeeModel.objects.filter(
                Q(id_num__icontains=search_q) |
                Q(position__icontains=search_q) |
                Q(user__first_name__icontains=search_q) |
                Q(user__last_name__icontains=search_q) |
                Q(user__email__icontains=search_q)
            ).order_by('user__username')
            return render(
                request,
                'admin_app/employees/employee_list.html',
                {'employee_list': employee_list}
            )


class EmployeeAddView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    """
    Class display and process a custom form allowing for
    addition of a new employee to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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
        employee_group = form.cleaned_data['user_group']
        new_employee.user.groups.set(employee_group)
        return super().form_valid(form)


class EmployeeEditView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class display and process a custom form allowing  for
    editting of an employee.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'admin_app.update_employeemodel'
    def get(self, request, pk):
        employee = EmployeeModel.objects.get(id=pk)
        user = User.objects.get(id=employee.user_id)
        form = EmployeeEditForm(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'employee_id': employee.id_num,
                'position': employee.position,
                'department': employee.section_id.all(),
                'user_email': user.email,
                'staff': user.is_staff,
            }
        )
        return render(
            request,
            'admin_app/employees/employeemodel_form.html',
            {'form': form}
        )

    def post(self, request, pk):
        form = EmployeeEditForm(request.POST)
        updated_user = User.objects.get(employee=pk)
        updated_employee = EmployeeModel.objects.get(id=pk)

        if form.is_valid():
            updated_user.first_name = form.cleaned_data['first_name']
            updated_user.last_name = form.cleaned_data['last_name']
            updated_user.email = form.cleaned_data['user_email']
            updated_user.is_staff = form.cleaned_data['staff']

            updated_employee.employee_id = form.cleaned_data['employee_id']
            updated_employee.position = form.cleaned_data['position']
            department = form.cleaned_data['department']
            updated_employee.section_id.set(department)

            updated_user.save()
            updated_employee.save()
            return redirect('employee_list')

        return render(
            request,
            'admin_app/employees/employeemodel_form.html',
            {'form': form},
        )


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting an employee from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'admin_app.delete_employeemodel'
    template_name = 'admin_app/employees/employeemodel_confirm_delete.html'
    model = EmployeeModel
    success_url = '/employee_list/'


# TODO: add current location
class TodayProductionView(View):
    """
    Class creates a view generating a production list for
    current day, with the option to lookup other days.
    """
    def get(self, request):
        form = DatePicker()
        now = datetime.now().strftime('%Y-%m-%d')
        output = ProductsModel.objects.filter(
            production_date__icontains=now,
        ).order_by('order_num', 'job_no', '-finished')
        return render(
            request,
            'admin_app/today_production.html',
            {
                'output': output,
                'form': form,
                'date': now,
            }
        )

    def post(self, request):
        form = DatePicker(request.POST)
        if form.is_valid():
            pick_date = form.cleaned_data['change_date']
            print(pick_date)
            output = ProductsModel.objects.filter(
                production_date__icontains=pick_date,
            ).order_by('order_num', 'job_no', '-finished')
            return render(
                request,
                'admin_app/today_production.html',
                {
                    'output': output,
                    'form': form,
                    'date': pick_date,
                }
            )

