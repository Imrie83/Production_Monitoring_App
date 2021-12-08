from django.db import models
from django.utils.html import mark_safe
from django.utils.html import escape


class ToolsModel(models.Model):
    """
    A model that stores tools info.
    """
    tool_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Tool name',
        help_text='Short tool name',
        unique=True,
    )
    type = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Type',
        help_text='PCD - HSS - Carbide',
        blank=True,
    )
    stock = models.IntegerField(
        verbose_name='In stock',
        null=False,
        default=0,
    )
    max_run_time = models.IntegerField(
        verbose_name='Allowed run time',
        null=False,
        default=0,
        help_text='Maximum run time allowed before tool change - in minutes!'
    )
    description = models.TextField(
        verbose_name='Description',
        null=True,
        blank=True,
    )
    img = models.ImageField(
        verbose_name='Image',
        name='image',
        null=True,
        blank=True,
        upload_to='static/img/tools/'
    )

    class Meta:
        verbose_name = 'Tool'
        verbose_name_plural = 'Tools'

    def short_description(self):
        return self.description[:50]

    short_description.short_description = 'Description'

    def __str__(self):
        return self.tool_name
