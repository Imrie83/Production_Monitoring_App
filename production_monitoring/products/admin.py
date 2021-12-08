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
    readonly_fields = [
        'show_all_lines',
    ]
    list_per_page = 20
    search_fields = [
        'order_number',
        'customer_id__customer_name',
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
        'door_type',
        'short_description',
        'stock',
    ]
    list_per_page = 20
    search_fields = [
        'name',
        'product_type',
        'door_type',
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
        'full_job_no',
        'door_type',
        'production_date',
        'delivery_date',
        'finished',
    ]
    list_per_page = 201
    search_fields = [
        'order_num__order_number',
        'door_type',
        'production_date',
        'delivery_date',
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
    list_per_page = 20
    search_fields = [
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
    list_per_page = 20
    search_fields = [
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
    list_per_page = 20
    search_fields = [
        'glass_name',
        'glass_door_type',
        'stock',
    ]
    ordering = [
        'glass_name',
    ]
