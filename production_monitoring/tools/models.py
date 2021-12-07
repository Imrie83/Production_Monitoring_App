from django.db import models


class ToolsModel(models.Model):
    """
    A model that stores tools info.
    """
    tool_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Tool name',
        help_text='Short tool name',
    )
    type = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Type',
        help_text='PCD - HSS - Carbide'
    )
    stock = models.IntegerField(
        verbose_name='In stock',
        null=False
    )
    max_run_time = models.IntegerField(
        verbose_name='Allowed run time',
        null=True,
        help_text='Maximum run time allowed before tool change - in minutes!'
    )
    description = models.TextField(
        verbose_name='Description',
        null=True,
    )
    img = models.ImageField(
        verbose_name='Image',
        name='image',
        null=True,
        upload_to='static/img/tools/'
    )

    class Meta:
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def __str__(self):
        return self.tool_name
