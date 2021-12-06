from django.db import models


class ToolsModel(models.Model):
    """
    A model that stores tools info.
    """
    tool_name = models.CharField(
        max_length=255,
        null=False,
        verbose_name='Tool name'
    )
    type = models.CharField(
        max_length=255,
        null=True,
        verbose_name='Type'
    )
    stock = models.IntegerField(
        verbose_name='In stock',
        null=False
    )
    wear_limit = models.IntegerField(
        verbose_name='Allowed use time',
        null=True,
    )
