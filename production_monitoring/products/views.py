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
            'products/order_list.html',
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
                'products/order_details.html',
                {'order_details': order_details}
            )
        except KeyError:
            return redirect('/order_list/')


class EditOrderView(PermissionRequiredMixin, UpdateView):
    """
    Class allowing to edit order details.
    """
    permission_required = 'products.update_ordermodel'
    model = OrderModel
    fields = '__all__'
    success_url = '/order_list/'


class DeleteOrderView(PermissionRequiredMixin, DeleteView):
    """
    class allowing to delete an order from database.
    """
    permission_required = 'products.delete_ordermodel'
    model = OrderModel
    success_url = '/order_list/'


class AddOrderView(PermissionRequiredMixin, CreateView):
    """
    Class allowing to create a new order line.
    """
    permission_required = 'products.add_ordermodel'
    model = OrderModel
    fields = '__all__'
    success_url = '/order_list/'



