from django.contrib import admin
from  tools.models import ToolsModel


@admin.register(ToolsModel)
class ToolsAdmin(admin.ModelAdmin):
    list_display = [
        'tool_name',
        'type',
        'description',
        'stock',
        'max_run_time',
    ]
