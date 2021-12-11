from django import forms
from django.contrib.auth.models import User, Group
from django.core.validators import validate_email, URLValidator
from django.core.exceptions import ValidationError
from tools.models import ToolsModel
from admin_app.models import EmployeeModel, DepartmentModel


class LoginForm(forms.Form):
    """
    Class creates login form to be displayed on main page
    """
    login = forms.CharField(label='Login')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


def employee_id_validator(value):
    """
    function validates employee ID number.
    :param value:
    :raise ValidationError:
    """
    if EmployeeModel.objects.filter(id_num=value):
        raise ValidationError('Employee ID taken!')


def username_validator(value):
    """
    function validates employees username
    :param value:
    :raise Validation Error:
    """
    if User.objects.filter(username=value):
        raise ValidationError('Username taken!')


class EmployeeAddForm(forms.Form):
    """
    Class defining a custom form allowing to add
    an employee information.
    :var: username
    :var: password_1
    :var: password_2
    :var: first_name
    :var: last_name
    :var: employee_id
    :var: position
    :var: department
    :var: user_email
    :var: staff
    """
    username = forms.CharField(
        label='User name',
        validators=[username_validator],
    )
    password_1 = forms.CharField(
        widget=forms.PasswordInput,
        label='Password',
    )
    password_2 = forms.CharField(
        widget=forms.PasswordInput,
        label='Repeat Password',
    )
    first_name = forms.CharField(
        label='Name'
    )
    last_name = forms.CharField(
        label='Surname'
    )
    user_group = forms.ModelMultipleChoiceField(
        label='Employee Permission Level',
        queryset=Group.objects.all(),
    )
    employee_id = forms.IntegerField(
        validators=[employee_id_validator],
        label='Employee ID',
    )
    position = forms.CharField(
        label='Position'
    )
    department = forms.ModelMultipleChoiceField(
        label='Department',
        queryset=DepartmentModel.objects.all(),
    )
    user_email = forms.EmailField(
        label='E-mail'
    )
    staff = forms.BooleanField(
        initial=True,
        required=False,
    )

    def clean(self):
        """
        method checking if both passwords match

        :return: cleaned_data
        """
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password_1')
        password2 = cleaned_data.get('password_2')
        if password1 != password2:
            raise ValidationError('Password does not match')
        return cleaned_data


class EmployeeEditForm(forms.Form):
    """
    Class defining a custom form allowing to edit
    an employee information.
    :var: username
    :var: password_1
    :var: password_2
    :var: first_name
    :var: last_name
    :var: employee_id
    :var: position
    :var: department
    :var: user_email
    :var: staff
    """

    first_name = forms.CharField(
        label='Name'
    )
    last_name = forms.CharField(
        label='Surname'
    )
    employee_id = forms.IntegerField(
        label='Employee ID',
    )
    position = forms.CharField(
        label='Position'
    )
    department = forms.ModelMultipleChoiceField(
        label='Department',
        queryset=DepartmentModel.objects.all(),
    )
    user_email = forms.EmailField(
        label='E-mail'
    )
    staff = forms.BooleanField(
        initial=True,
        required=False,
    )
