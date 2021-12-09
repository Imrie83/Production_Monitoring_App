from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, CreateView, DetailView, UpdateView

from tools.models import ToolsModel
from tools.forms import AddToolForm


class ToolListView(View):
    """
    Class displaying a list of all tools
    available in database
    """
    def get(self, request):
        tool_list = ToolsModel.objects.all()

        return render(
            request,
            'tools/tool_list.html',
            {'tool_list': tool_list}
        )


class AddToolView(PermissionRequiredMixin, CreateView):
    """
    Class display a form allowing
    to add a new tool to database.
    """
    permission_required = 'tools.add_toolsmodel'
    model = ToolsModel
    fields = '__all__'
    success_url = '/tool_list/'


class EditToolView(PermissionRequiredMixin, UpdateView):
    """
    Class display a form allowing
    to edit a tool in database.
    """
    permission_required = 'tools.update_toolsmodel'
    model = ToolsModel
    fields = '__all__'
    success_url = '/tool_list/'


class DeleteToolView(PermissionRequiredMixin, DetailView):
    """
    Class allows to delete
    a tool from database
    """
    permission_required = 'tools.delete_toolsmodel'
    model = ToolsModel
    success_url = '/tool_list/'
