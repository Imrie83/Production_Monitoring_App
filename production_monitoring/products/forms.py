from django import forms
from django.core.validators import validate_email, URLValidator
from django.core.exceptions import ValidationError


from products.models import (
    ComponentsModel,
    ComponentToolsModel,
    GlassModel,
    GlassToolModel, ProductsModel, ProductComponent,
)


class ProductAddForm(forms.ModelForm):
    """
    Class creating a custom form
    for adding product lines to order.
    """
    class Meta:
        model = ProductsModel
        exclude = ['components']


class ProductEditForm(forms.ModelForm):
    """
    Class creating a custom form
    allowing to edit a door line.
    """
    class Meta:
        model = ProductsModel
        exclude = ['components']

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


class ProductComponentAddForm(forms.ModelForm):
    """
    Class creates a custom form used to add
    components to each door
    """
    class Meta:
        model = ProductComponent
        fields = '__all__'

    # TODO: figure out validation.
    # def clean(self):
    #     """
    #     Validate door and glass types do match.
    #     """
    #     cleaned_data = super().clean()
    #     product = cleaned_data.get('product_id')
    #     print(product)
    #     component = cleaned_data.get('component_id')
    #     print(component)
    #     # if product.door_type != component.door_type:
    #     #     raise ValidationError('test message')
    #     # if self.component_id.door_type != product.door_type:
    #     #     raise ValidationError('Door and Component types must match!')



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
