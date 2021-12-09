from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from products.models import (
    OrderModel,
    ProductsModel,
    ComponentsModel,
    CustomerModel,
    DoorStyleModel,
    GlassModel,
)


class OrderListView(View):
    """
    Class display a list of all orders
    available in database.
    """
    def get(self, request):
        orders = OrderModel.objects.all()
        return render(
            request,
            'products/orders/order_list.html',
            {'orders': orders}
        )


class OrderDetailView(View):
    """
    Class display a detailed view of each order.
    """
    def get(self, request, pk):
        try:
            order_details = OrderModel.objects.get(id=pk)
            return render(
                request,
                'products/orders/order_details.html',
                {'order_details': order_details}
            )
        except KeyError:
            return redirect('/order_list/')


class EditOrderView(PermissionRequiredMixin, UpdateView):
    """
    Class allowing to edit order details.
    """
    permission_required = 'products.update_ordermodel'
    template_name = 'products/orders/ordermodel_form.html'
    model = OrderModel
    fields = '__all__'
    success_url = '/order_list/'


class DeleteOrderView(PermissionRequiredMixin, DeleteView):
    """
    class allowing to delete an order from database.
    """
    permission_required = 'products.delete_ordermodel'
    template_name = 'products/orders/ordermodel_confirm_delete.html'
    model = OrderModel
    success_url = '/order_list/'


class AddOrderView(PermissionRequiredMixin, CreateView):
    """
    Class allowing to create a new order line.
    """
    permission_required = 'products.add_ordermodel'
    template_name = 'products/orders/ordermodel_form.html'
    model = OrderModel
    fields = '__all__'
    success_url = '/order_list/'


class ComponentListView(View):
    """
    Class display a list of all components available.
    """
    def get(self, request):
        component_list = ComponentsModel.objects.all()
        return render(
            request,
            'products/components/component_list.html',
            {'component_list': component_list}
        )


class ComponentDetailView(View):
    """
    Class displaying component details.
    """
    def get(self, request, pk):
        try:
            component_details = ComponentsModel.objects.get(id=pk)
            return render(
                request,
                'products/components/component_details.html',
                {'component_details': component_details}
            )
        except KeyError:
            return redirect('/component_list/')


class AddComponentView(PermissionRequiredMixin, CreateView):
    """
    Class displaying form allowing to add a new component
    in to the database.
    """
    permission_required = 'products.add_componentsmodel'
    template_name = 'products/components/componentsmodel_form.html'
    model = ComponentsModel
    fields = '__all__'
    success_url = '/component_list/'


class EditComponentView(PermissionRequiredMixin, UpdateView):
    """
    Class display a form allowing to update information
    about a component.
    """
    permission_required = 'products.edit_componentsmodel'
    template_name = 'products/components/componentsmodel_form.html'
    model = ComponentsModel
    fields = '__all__'
    success_url = '/component_list/'


class DeleteComponentView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a component.
    """
    permission_required = 'products.delete_componentsmodel'
    template_name = 'products/components/componentsmodel_confirm_delete.html'
    model = ComponentsModel
    success_url = '/component_list/'


class GlassListView(View):
    """
    Class display a list of all
    glass available.
    """
    def get(self, request):
        glass_list = GlassModel.objects.all()
        return render(
            request,
            'products/glass/glass_list.html',
            {'glass_list': glass_list}
        )


class GlassDetailView(View):
    """
    Class display detailed view of
    specific glass.
    """
    def get(self, request, pk):
        try:
            glass_detail = GlassModel.objects.get(id=pk)
            return render(
                request,
                'products/glass/glass_details.html',
                {'glass_detail': glass_detail}
            )
        except KeyError:
            return redirect('/glass_list/')


class GlassAddView(PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new piece of glass  to database.
    """
    permission_required = 'products.add_glassmodel'
    template_name = 'products/glass/glassmodel_form.html'
    model = GlassModel
    fields = '__all__'
    success_url = '/glass_list/'


class GlassEditView(PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit glass information.
    """
    permission_required = 'products.edit_glassmodel'
    template_name = 'products/glass/glassmodel_form.html'
    model = GlassModel
    fields = '__all__'
    success_url = '/glass_list/'


class GlassDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a piece of glass from database.
    """
    permission_required = 'products.delete_glassmodel'
    template_name = 'products/glass/glassmodel_confirm_delete.html'
    model = GlassModel
    success_url = '/glass_list/'


class StyleListView(View):
    """
    Class display a list of all
    styles available.
    """
    def get(self, request):
        style_list = DoorStyleModel.objects.all()
        return render(
            request,
            'products/styles/style_list.html',
            {'style_list': style_list}
        )


class StyleDetailView(View):
    """
    Class display detailed view of
    specific door style.
    """
    def get(self, request, pk):
        try:
            style_detail = DoorStyleModel.objects.get(id=pk)
            return render(
                request,
                'products/styles/style_details.html',
                {'style_detail': style_detail}
            )
        except KeyError:
            return redirect('/style_list/')


class StyleAddView(PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new door style to database.
    """
    permission_required = 'products.add_doorstylemodel'
    template_name = 'products/styles/doorstylemodel_form.html'
    model = DoorStyleModel
    fields = '__all__'
    success_url = '/style_list/'


class StyleEditView(PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit style information.
    """
    permission_required = 'products.edit_doorstylemodel'
    template_name = 'products/styles/doorstylemodel_form.html'
    model = DoorStyleModel
    fields = '__all__'
    success_url = '/style_list/'


class StyleDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a door style from database.
    """
    permission_required = 'products.delete_doorstylemodel'
    template_name = 'products/styles/doorstylemodel_confirm_delete.html'
    model = DoorStyleModel
    success_url = '/style_list/'
