from django.contrib import admin
from forms import UserForm
from admin_app.models import (
    EmployeeModel,
    DepartmentModel,
    MachineModel,
)


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Class register EmployeeModel in Admin panel.
    :model: `EmployeeModel`
    """
    list_display = [
        'display_employee_name',
        'id_num',
        'show_all_departments',
        'position',
    ]
    list_per_page = 20


@admin.register(DepartmentModel)
class DepartmentAdmin(admin.ModelAdmin):
    """
    Class register DepartmentModel in Admin panel.
    :model: `DepartmentModel
    """
    form = UserForm
    list_per_page = 20


@admin.register(MachineModel)
class MachineAdmin(admin.ModelAdmin):
    """
    Class register MachineModel in Admin panel.
    :model: `MachineModel`
    """
    list_display = ['name', 'machine_location']
    search_fields = ['name', 'machine_location']
    list_per_page = 20
