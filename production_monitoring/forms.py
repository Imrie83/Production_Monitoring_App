from django import forms
from django.core.exceptions import ValidationError
from admin_app.models import DepartmentModel, EmployeeModel


class UserForm(forms.ModelForm):

    class Meta:
        model = DepartmentModel
        fields = ['section_name']

