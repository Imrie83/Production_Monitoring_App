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


class OrderModel(models.Model):
    """
    Model stores JOB numbers and customers associated.
    """
    order_number = models.CharField(
        max_length=20,
        null=False,
        default='JOB',
        verbose_name='Order Num.',
        help_text='order num. format - "JOB0000000"',
        unique=True,
    )
    customer_id = models.ForeignKey(
        to='CustomerModel',
        null=False,
        on_delete=models.CASCADE,
        default=0,
        verbose_name='Customer'
    )

    class Meta:
        verbose_name = 'Order',
        verbose_name_plural = 'Orders',

    @property
    def show_all_lines(self):
        lines = ProductsModel.objects.filter(order_num=self.id)
        output = ''
        for line in lines:
            output += f'{line}\n'
        return output

    def __str__(self):
        return self.order_number


class ComponentsModel(models.Model):
    """
    A model storing information about components.
    :model: `tools.ToolsModel`
    """
    name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Component name',
        unique=True,
    )
    stock = models.IntegerField(
        verbose_name='Stock',
        null=False,
        default=0,
    )
    tools_req = models.ManyToManyField(
        to=ToolsModel,
        through='ComponentToolsModel',
        verbose_name='Tools Required'
    )
    door_type = models.CharField(
        choices=DOOR_TYPES,
        verbose_name='Door type',
        max_length=255,
        default=DOOR_TYPES[0]
    )
    product_type = models.IntegerField(
        choices=PRODUCT_TYPE,
        verbose_name='Type',
        default=PRODUCT_TYPE[0]
    )
    component_description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Component description'
    )
    img = models.ImageField(
        verbose_name='Image',
        null=True,
        blank=True,
        upload_to='static/img/fixtures',
    )

    class Meta:
        verbose_name = 'Component'
        verbose_name_plural = 'Components'

    def short_description(self):
        return self.component_description[:50]

    def __str__(self):
        return f'{self.name}'


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
    order_num = models.ForeignKey(
        to=OrderModel,
        null=True,
        verbose_name='Order number',
        on_delete=models.CASCADE,
    )
    job_no = models.CharField(
        max_length=4,
        null=False,
        unique=True,
        verbose_name='Line number',
        help_text='four digit line number',
        default='0000',
    )
    door_type = models.CharField(
        choices=DOOR_TYPES,
        verbose_name='Type',
        max_length=255,
        default='Select Type',
        null=False
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
    door_width = models.FloatField(
        verbose_name='Door width',
        null=False,
        default=0,
    )
    door_height = models.FloatField(
        verbose_name='Door height',
        null=False,
        default=0,
    )
    delivery_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Delivery date',
    )
    delivery_address = models.TextField(
        verbose_name='Delivery address',
        null=True,
        blank=True,
    )
    machining_time = models.IntegerField(
        null=True,
        verbose_name='Total machining time',
        editable=False,
    )
    production_date = models.DateField(
        verbose_name='Production date',
        null=True,
        blank=True,
    )
    finished = models.BooleanField(
        verbose_name='Finished?',
        editable=False,
        null=True,
        default=False,
    )

    class Meta:
        verbose_name = 'Door Order'
        verbose_name_plural = 'Door Orders'
        unique_together = ['order_num', 'job_no']

    def full_job_no(self):
        return f'{self.order_num}-{self.job_no}'

    full_job_no.short_description = 'Job number'

    def __str__(self):
        return self.full_job_no


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

    class Meta:
        verbose_name = 'Door component'
        verbose_name_plural = 'Door compoonents'


class CustomerModel(models.Model):
    """
    Model stores information about customers
    """
    customer_name = models.CharField(
        max_length=255,
        verbose_name='Customer name',
        null=False,
    )
    customer_email = models.EmailField(
        verbose_name='e-mail',
        null=True,
        blank=True,
    )
    customer_phone = models.CharField(
        max_length=30,
        verbose_name='Phone no.',
        null=True,
        blank=True,
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
        choices=DOOR_TYPES,
        max_length=255,
        verbose_name='Door type',
        null=False,
    )
    img = models.ImageField(
        verbose_name='Image',
        upload_to='static/img/styles/',
        blank=True
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
        unique=True,
    )
    glass_door_type = models.CharField(
        max_length=255,
        choices=DOOR_TYPES,
        default=DOOR_TYPES[0],
        verbose_name='Door type',
    )
    tools_req = models.ManyToManyField(
        to=ToolsModel,
        through='GlassToolModel',
        verbose_name='Tools Required'
    )
    stock = models.IntegerField(
        null=False,
        default=0,
        verbose_name='In stock'
    )
    description = models.TextField(
        null=True,
        verbose_name='Description',
        blank=True,
    )
    img = models.ImageField(
        null=True,
        verbose_name='Image',
        upload_to='static/img/glass/',
        blank=True,
    )

    class Meta:
        verbose_name = 'Glass'
        verbose_name_plural = 'Glass'

    def short_description(self):
        return self.description[:50]

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
