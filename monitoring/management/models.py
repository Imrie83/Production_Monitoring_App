from django.db import models
from django.contrib.auth.models import User
from products.models import ProductsModel


class EmployeeModel(models.Model):
    """
    Models extends User model by additional information
    :model: `auth.User`
    :model: `management.SectionModel`
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    section_id = models.ForeignKey(
        to='SectionModels',
        null=False,
        verbose_name='Section',
        on_delete=models.CASCADE
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

    def __str__(self):
        return f'{self.user}'


class UserProductModel(models.Model):
    """
    Models saves information which user has been working on an order
    and at what time / date
    :models: `products.ProductModel`
    :models: `management.EmployeeModel
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


class SectionModels(models.Model):
    """
    Model saves information about employees in each section in the company
    :models: `management.EmployeeModel`
    """
    employee_id = models.ManyToManyField(
        to=EmployeeModel,
        related_name='section'
    )
    section_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Section'
    )

    def __str__(self):
        return self.section_name