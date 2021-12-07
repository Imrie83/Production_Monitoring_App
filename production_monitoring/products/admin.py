from django.contrib import admin
from products.models import (
    ComponentsModel,
    ProductsModel,
    ComponentToolsModel,
    GlassToolModel,
    ProductComponent,
    CustomerModel,
    DoorStyleModel,
    GlassModel,
    OrderModel,
)


class ComponentToolInline(admin.TabularInline):
    """
    Class setting inline selection of component
    tools from transient model.
    :models: `ComponentToolsModel`
    """
    model = ComponentToolsModel


class GlassToolInline(admin.TabularInline):
    """
    Class setting inline selection of glass
    tools from transient model.
    :models: `GlassToolModel`
    """
    model = GlassToolModel


class ProductComponentInline(admin.TabularInline):
    """
    Class setting inline selection of product
    components from transient model.
    :models: `ProductComponent`
    """
    model = ProductComponent


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    """
    Class registering OrderModel in Admin panel.
    :models: `OrderModel`
    """
    list_display = [
        'order_number',
        'customer_id',
    ]


@admin.register(ComponentsModel)
class ComponentsAdmin(admin.ModelAdmin):
    """
    Class registering ComponentsModel in Admin panel.
    :models: `ComponentsModel`
    """
    inlines = [
      ComponentToolInline,
    ]

    list_display = [
        'name',
        'product_type',
        'component_description',
        'stock',
    ]


@admin.register(ProductsModel)
class ProductAdmin(admin.ModelAdmin):
    """
    Class registering ProductModel in Admin Panel.
    :models: `ProductsModel`
    """
    inlines = [
        ProductComponentInline,
    ]

    list_display = [
        'job_no',
        'door_type',
        'production_date',
        'machining_time',
    ]


@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    """
    Class registering CustomerModel in Admin panel.
    :models: `CustomerModel`
    """
    list_display = [
        'customer_name',
        'customer_email',
        'customer_phone',
    ]


@admin.register(DoorStyleModel)
class DoorStyleAdmin(admin.ModelAdmin):
    """
    Class registering DoorStyleModel in Admin panel.
    :models: `DoorStyleModel`
    """
    list_display = [
        'style_name',
        'style_type',
    ]


@admin.register(GlassModel)
class GlassAdmin(admin.ModelAdmin):
    """
    Class registering GlassModel in Admin panel.
    :models: `GlassModel`
    """
    inlines = [
        GlassToolInline,
    ]

    list_display = [
        'glass_name',
        'glass_door_type',
        'stock',
        'description',
    ]
    search_fields = ['glass_name', 'glass_door_type']
    ordering = ['glass_name']