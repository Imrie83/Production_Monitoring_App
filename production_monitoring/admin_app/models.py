from django.db import models
from django.contrib.auth.models import User
from products.models import ProductsModel


class MachineModel(models.Model):
    """
    Model stores names of machines in the company
    """
    name = models.CharField(
        max_length=255,
        verbose_name='CNC name',
        null=False,
        unique=True,
    )
    machine_location = models.ForeignKey(
        to='DepartmentModel',
        verbose_name='Machine location',
        null=True,
        on_delete=models.SET(None),
    )

    class Meta:
        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    def __str__(self):
        return self.name


class MachineEmployeeModel(models.Model):
    machine_id = models.ForeignKey(
        to=MachineModel,
        on_delete=models.SET_NULL,
        null=True,
    )
    employee_id = models.ForeignKey(
        to='EmployeeModel',
        on_delete=models.SET_NULL,
        null=True,
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class EmployeeModel(models.Model):
    """
    Models extends User model by additional information
    :model: `auth.User`
    :model: `admin_app.DepartmentModel`
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    id_num = models.IntegerField(
        verbose_name='Employee id number',
        null=False,
        default=None,
    )
    section_id = models.ManyToManyField(
        to='DepartmentModel',
        related_name='employees',
        verbose_name='Department name',
    )
    position = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Position'
    )
    products = models.ManyToManyField(
        to=ProductsModel,
        through='UserProductModel',
    )
    machine = models.ManyToManyField(
        to=MachineModel,
        through=MachineEmployeeModel,
        verbose_name='Machine used',
        editable=False,
    )

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f'{self.user}'


class UserProductModel(models.Model):
    """
    Models saves information which user has been working on an order
    and at what time / date
    :models: `products.ProductModel`
    :models: `admin_app.EmployeeModel
    """
    product_id = models.ForeignKey(
        ProductsModel,
        on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        to=EmployeeModel,
        on_delete=models.CASCADE
    )
    prod_start = models.DateTimeField(
        verbose_name='Work started',
        null=True,
    )
    prod_end = models.DateTimeField(
        verbose_name='Work ended',
        null=True
    )


class DepartmentModel(models.Model):
    """
    Model storing sections in the company
    """
    section_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Department'
    )

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.section_name
