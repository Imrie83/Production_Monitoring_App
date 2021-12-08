from django.contrib import admin
from tools.models import ToolsModel
from django.utils.html import format_html, mark_safe


@admin.register(ToolsModel)
class ToolsAdmin(admin.ModelAdmin):
    """
    Class register ToolsModel in Admin Panel
    :models: `ToolsModel`
    """
    list_display = [
        'tool_name',
        'type',
        'short_description',
        'stock',
        'max_run_time',
    ]

    list_per_page = 20
    ordering = ['tool_name']
    search_fields = ['tool_name', 'type', 'stock']
