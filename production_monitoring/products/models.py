from django.db import models
from tools.models import ToolsModel

DOOR_TYPES = (
    ('firedoor', 'Firesafe line'),
    ('regency', 'Regency line'),
    ('script', 'Script line'),
)

PRODUCT_TYPE = (
    (1, 'Lock'),
    (2, 'Handle'),
    (3, 'Viewer'),
    (4, 'Knocker'),
    (5, 'Letter plate'),
    (6, 'Hinges'),
    (7, 'Apertures'),
    (8, 'Numerals'),
)

DOOR_COLOR = (
    ('white', 'White'),
    ('green', 'Green'),
    ('black', 'Black'),
    ('blue', 'Blue'),
    ('red', 'Red'),
    ('rosewood', 'Rosewood'),
    ('oak', 'Oak'),
)

HANDING = (
    ('LI', 'Left - Open In'),
    ('LO', 'Left - Open Out'),
    ('RI', 'Right - Open In'),
    ('RO', 'Right - Open Out'),
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
    door_type = models.CharField(
        choices=DOOR_TYPES,
        verbose_name='Type',
        max_length=255,
        default='Select Type'
    )
    component_description = models.TextField(
        null=True,
        verbose_name='Component description'
    )
    product_type = models.IntegerField(
        choices=PRODUCT_TYPE,
        verbose_name='Type'
    )
    img = models.ImageField(
        verbose_name='Image',
        null=True,
    )

    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'

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

    class Meta:
        verbose_name = 'Component Tool'
        verbose_name_plural = 'Component Tools'


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
    color = models.CharField(
        choices=DOOR_COLOR,
        verbose_name='Door colour',
        null=False,
        max_length=255,
        default=DOOR_COLOR[0]
    )
    style = models.ForeignKey(
        to='DoorStyleModel',
        verbose_name='Door style',
        null=False,
        on_delete=models.SET('None'),
        default=None,
    )
    glass = models.ForeignKey(
        to='GlassModel',
        verbose_name='Glass',
        null=False,
        on_delete=models.SET('None'),
        default=None,
    )
    components = models.ManyToManyField(
        to=ComponentsModel,
        through='ProductComponent',
        related_name='product',
    )
    handing = models.CharField(
        choices=HANDING,
        verbose_name='Door handing',
        null=False,
        max_length=255,
        default=HANDING[0],
    )
    customer_id = models.ForeignKey(
        to='CustomerModel',
        null=False,
        on_delete=models.CASCADE,
        default=0,
    )
    delivery_date = models.DateField(
        null=True,
        verbose_name='Delivery date',
    )
    delivery_address = models.TextField(
        verbose_name='Delivery address',
        null=True,
    )
    machining_time = models.IntegerField(
        null=True,
        verbose_name='Total machining time'
    )
    frame_size = models.IntegerField(
        null=False,
        verbose_name='Frame total length'
    )
    production_date = models.DateField(
        verbose_name='Production date',
        null=True
    )
    door_type = models.CharField(
        choices=DOOR_TYPES,
        verbose_name='Type',
        max_length=255,
        default='Select Type',
        null=False
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.job_no


class ProductComponent(models.Model):
    """
    Model storing count of components required in a given product
    :models: `ProductModel`,
    :models: `ComponentsModel`,
    """
    product_id = models.ForeignKey(
        to=ProductsModel,
        on_delete=models.CASCADE,
    )
    component_id = models.ForeignKey(
        to=ComponentsModel,
        on_delete=models.CASCADE,
    )
    count = models.IntegerField(
        verbose_name='Component count'
    )


class CustomerModel(models.Model):
    """
    Model stores information about customers
    """
    customer_name = models.CharField(
        max_length=255,
        verbose_name='Customer name',
        null=False,
    )
    customer_email = models.CharField(
        max_length=50,
        verbose_name='e-mail',
        null=True,
    )
    customer_phone = models.CharField(
        max_length=30,
        verbose_name='Phone no.',
        null=True,
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.customer_name}'


class DoorStyleModel(models.Model):
    """
    Model storing door style information
    """
    style_name = models.CharField(
        max_length=255,
        verbose_name='Style',
        null=False,
    )
    style_type = models.CharField(
        max_length=255,
        verbose_name='Door type',
        null=False,
    )
    img = models.ImageField(
        verbose_name='Image',
    )

    class Meta:
        verbose_name = 'Door Style'
        verbose_name_plural = 'Door Styles'

    def __str__(self):
        return f'{self.style_name} - door type: {self.style_type}'


class GlassModel(models.Model):
    """
    Model stores information about glass types available
    :models: `ToolsModel`
    """
    glass_name = models.CharField(
        max_length=255,
        verbose_name='Glass name',
        null=False,
    )
    glass_door_type = models.CharField(
        max_length=255,
        choices=DOOR_TYPES,
        default=DOOR_TYPES[0],
        verbose_name='for door type',
    )
    tools_req = models.ManyToManyField(
        to=ToolsModel,
        through='GlassToolModel',
        verbose_name='Tools Required'
    )
    stock = models.IntegerField(
        null=False,
        verbose_name='In stock'
    )
    description = models.TextField(
        null=True,
        verbose_name='Description'
    )
    img = models.ImageField(
        null=True,
        verbose_name='Image'
    )

    class Meta:
        verbose_name = 'Glass'
        verbose_name_plural = 'Glass'

    def __str__(self):
        return f'{self.glass_name} - door type allowed: {self.glass_door_type}'


class GlassToolModel(models.Model):
    """
    Model storing machining time for each tool on a glass
    :model: `products.ComponentsModel`
    :model: `tools.ToolsModel`
    """
    glass_id = models.ForeignKey(
        GlassModel,
        on_delete=models.CASCADE,
        related_name='glass'
    )
    tool_id = models.ForeignKey(
        ToolsModel,
        on_delete=models.CASCADE,
        related_name='glass_tool'
    )
    machine_time = models.IntegerField()

    class Meta:
        verbose_name = 'Aperture Tool'
        verbose_name_plural = 'Aperture Tools'
