from django.contrib import admin
from forms import UserForm
from admin_app.models import (
    EmployeeModel,
    DepartmentModel,
    MachineModel,
)


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(DepartmentModel)
class SectionAdmin(admin.ModelAdmin):
    form = UserForm


@admin.register(MachineModel)
class MachineAdmin(admin.ModelAdmin):
    list_display = ['name']
