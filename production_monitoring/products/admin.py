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
    model = ComponentToolsModel


class GlassToolInline(admin.TabularInline):
    model = GlassToolModel


class ProductComponentInline(admin.TabularInline):
    model = ProductComponent


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'customer_id',
    ]


@admin.register(ComponentsModel)
class ComponentsAdmin(admin.ModelAdmin):

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
    list_display = [
        'customer_name',
        'customer_email',
        'customer_phone',
    ]


@admin.register(DoorStyleModel)
class DoorStyleAdmin(admin.ModelAdmin):
    list_display = [
        'style_name',
        'style_type',
    ]


@admin.register(GlassModel)
class GlassAdmin(admin.ModelAdmin):
    inlines = [
        GlassToolInline,
    ]

    list_display = [
        'glass_name',
        'glass_door_type',
        'stock',
        'description',
    ]