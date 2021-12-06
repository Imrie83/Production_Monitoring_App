from django.db import models
from tools.models import ToolsModel

PRODUCT_TYPES = (
    ('firedoor', 'Firesafe door'),
    ('smc', 'Entrance door'),
)


class ComponentsModel(models.Model):
    """
    A model storing information about components.
    :model: `tools.ToolsModel`
    """
    name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Component name'
    )
    stock = models.IntegerField(verbose_name='Stock')
    tools_req = models.ManyToManyField(
        to=ToolsModel,
        through='ComponentToolsModel',
        verbose_name='Tools Required'
    )
    product_type = models.CharField(
        choices=PRODUCT_TYPES,
        verbose_name='Type',
        max_length=255,
        default='Select Type'
    )

    component_description = models.TextField(
        null=True,
        verbose_name='Component description'
    )

    def __str__(self):
        return f'{self.name} - {self.component_description[:30]}'


class ComponentToolsModel(models.Model):
    """
    Model storing machining time for each tool on a component
    :model: `products.ComponentsModel`
    :model: `tools.ToolsModel`
    """
    component_id = models.ForeignKey(
        ComponentsModel,
        on_delete=models.CASCADE,
        related_name='component'
    )
    tools_id = models.ForeignKey(
        ToolsModel,
        on_delete=models.CASCADE,
        related_name='tool'
    )
    machine_time = models.IntegerField()


class ProductsModel(models.Model):
    """
    Model storing information about products
    :model: `products.ComponentsModel`
    """
    job_no = models.CharField(
        max_length=30,
        null=False,
        unique=True,
        verbose_name='Job number'
    )
    machining_time = models.IntegerField(
        null=True,
        verbose_name='Total machining time'
    )
    frame_size = models.IntegerField(
        null=False,
        verbose_name='Frame total length'
    )
    components = models.ManyToManyField(
        to=ComponentsModel,
        related_name='product',
    )
    production_date = models.DateField(
        verbose_name='Production date',
        null=True
    )
    product_type = models.CharField(
        choices=PRODUCT_TYPES,
        verbose_name='Type',
        max_length=255,
        default='Select Type'
    )

    def __str__(self):
        return self.job_no

