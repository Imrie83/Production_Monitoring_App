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
            'admin_app/tool_list.html',
            {'tool_list': tool_list}
        )


class AddToolView(FormView):
    """
    Class display a form allowing
    to add a new tool to database.
    """
    template_name = 'admin_app/add_tool.html'
    form_class = AddToolForm
    success_url = '/tools/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
