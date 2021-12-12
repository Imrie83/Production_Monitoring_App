from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email, URLValidator
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, inlineformset_factory, \
    CheckboxSelectMultiple

from products.models import ComponentsModel, ComponentToolsModel, ProductsModel
from tools.models import ToolsModel


class ComponentToolForm(forms.ModelForm):
    class Meta:
        model = ComponentToolsModel
        exclude = []


class ComponentAddForm(forms.ModelForm):
    class Meta:

        model = ComponentsModel
        fields = [
            'name',
            'stock',
            'door_type',
            'product_type',
            'component_description',
            'img',
            'tools_req'
        ]
    # tools_req = forms.ModelMultipleChoiceField(
    #     queryset=ToolsModel.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )

    #     tools_req = forms.ModelMultipleChoiceField(queryset=ToolsModel.objects.all(), widget=forms.CheckboxSelectMultiple)


# ComponentToolFormSet = inlineformset_factory(
#     ToolsModel, ComponentToolsModel, form=ComponentAddForm,
#     fields=['tools_id', 'machine_time'], extra=1, can_delete=True
#     )


class ScanProductionForm(forms.Form):
    """
    Class defining a form used to scann a door
    by the staf on start their work.
    """
    job_no = forms.CharField(
        max_length=255,
        required=True,
    )


class ProductAddForm(forms.Form):
    """
    Class creating a custom product form
    """
    pass


class ComponentAddForm(forms.Form):
    """
    Class creating a custom component form
    """
