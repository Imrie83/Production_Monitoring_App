from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
)
from tools.models import ToolsModel


class ToolListView(View):
    """
    Class displaying a list of all tools
    available in database
    """
    def get(self, request):
        tool_list = ToolsModel.objects.order_by('tool_name')

        return render(
            request,
            'tools/tool_list.html',
            {'tool_list': tool_list}
        )

    def post(self, request):
        if 'search' in request.POST:
            search_q = request.POST['search']
            tool_list = ToolsModel.objects.filter(
                Q(tool_name__icontains=search_q) |
                Q(type__icontains=search_q)
            ).order_by('tool_name')
            return render(
                request,
                'tools/tool_list.html',
                {'tool_list': tool_list}
            )


class ToolDetailsView(LoginRequiredMixin, View):
    """
    Class displaying detailed information
    regarding an individual tool.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        try:
            tool_list = ToolsModel.objects.order_by('tool_name')
            tool_details = ToolsModel.objects.get(id=pk)
            return render(
                request,
                'tools/toolsmodel_detail.html',
                {'tool_details': tool_details, 'tool_list': tool_list}
            )
        except KeyError:
            return redirect('/tool_list/')

    def post(self, request, pk):
        if 'search' in request.POST:
            search_q = request.POST['search']
            tool_list = ToolsModel.objects.filter(
                Q(tool_name__icontains=search_q) |
                Q(type__icontains=search_q)
            ).order_by('tool_name')
            return render(
                request,
                'tools/tool_list.html',
                {'tool_list': tool_list}
            )


class AddToolView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class display a form allowing
    to add a new tool to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'tools.add_toolsmodel'
    model = ToolsModel
    fields = '__all__'
    success_url = '/tool_list/'


class EditToolView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display a form allowing
    to edit a tool in database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'tools.update_toolsmodel'
    model = ToolsModel
    fields = '__all__'
    success_url = '/tool_list/'


class DeleteToolView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class allows to delete
    a tool from database
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'tools.delete_toolsmodel'
    model = ToolsModel
    success_url = '/tool_list/'
