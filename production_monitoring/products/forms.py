from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email, URLValidator
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet, inlineformset_factory, \
    CheckboxSelectMultiple, formset_factory

from products.models import ComponentsModel, ComponentToolsModel, ProductsModel, \
    OrderModel, DOOR_TYPES, PRODUCT_TYPE, GlassModel, GlassToolModel
from tools.models import ToolsModel


class GlassAddForm(forms.ModelForm):
    """
    Class creating a custom form allowing
    to add a new piece of glass to the database.
    """
    class Meta:
        model = GlassModel
        exclude = ['tools_req']


class GlassToolAddForm(forms.ModelForm):
    """
    Class creating a custom form allowing to add
    required tools with machining times to the
    glass.
    """
    class Meta:
        model = GlassToolModel
        exclude = ['glass_id']


class ComponentAddForm(forms.ModelForm):
    """
    Class creating a custom form allowing to add a new component
    to database.
    """
    class Meta:

        model = ComponentsModel
        fields = [
            'name',
            'stock',
            'door_type',
            'product_type',
            'component_description',
            'img',
        ]


class ComponentToolsForm(forms.ModelForm):
    """
    Class displaying a custom form
    allowing to add tool required to machine
    a particular component together with
    machining time.
    """
    class Meta:
        model = ComponentToolsModel
        exclude = ['component_id']


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
    # order = forms.ChoiceField(
    #     choices=OrderModel.objects.all(),
    #
    # )
    # class Meta:
    #     model = ProductsModel
    #     exclude = []
