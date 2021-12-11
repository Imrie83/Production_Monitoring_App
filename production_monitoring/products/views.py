from datetime import datetime
from django.utils import timezone

from django.contrib.admin import TabularInline
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
import re

from admin_app.models import UserProductModel, EmployeeModel
from products.forms import ComponentAddForm, ScanProductionForm
from products.models import (
    OrderModel,
    ProductsModel,
    ComponentsModel,
    CustomerModel,
    DoorStyleModel,
    GlassModel, ComponentToolsModel,
)
from tools.models import ToolsModel


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

# TODO: figure out many-to-many with additional fields!
# class AddComponentView(PermissionRequiredMixin, CreateView):
#     """
#     Class displaying form allowing to add a new component
#     in to the database.
#     """
#     permission_required = 'products.add_componentsmodel'
#     template_name = 'products/components/componentsmodel_form.html'
#     model = ComponentsModel
#     fields = '__all__'
#     success_url = '/component_list/'


class AddComponentView(PermissionRequiredMixin, CreateView):
    """
    Class displaying form allowing to add a new component
    in to the database.
    """
    permission_required = 'products.add_componentsmodel'
    template_name = 'products/components/componentsmodel_form.html'
    model = ComponentsModel
    # fields = '__all__'
    form_class = ComponentAddForm
    success_url = '/component_list/'


#
# class AddComponentView(PermissionRequiredMixin, FormView):
#     permission_required = 'products.add_componentsmodel'
#     template_name = 'products/components/componentsmodel_form.html'
#     form_class = ComponentAddForm
#     success_url = '/component_list/'
#
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


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


class CustomerListView(View):
    """
    Class display a list of all
    customers available.
    """
    def get(self, request):
        customer_list = CustomerModel.objects.all()
        return render(
            request,
            'products/customers/customer_list.html',
            {'customer_list': customer_list}
        )


class CustomerDetailView(View):
    """
    Class display detailed view of
    specific customer.
    """
    def get(self, request, pk):
        try:
            customer_detail = CustomerModel.objects.get(id=pk)
            return render(
                request,
                'products/customers/customer_details.html',
                {'customer_detail': customer_detail}
            )
        except KeyError:
            return redirect('/customer_list/')


class CustomerAddView(PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new customer to database.
    """
    permission_required = 'products.add_customermodel'
    template_name = 'products/customers/customermodel_form.html'
    model = CustomerModel
    fields = '__all__'
    success_url = '/customer_list/'


class CustomerEditView(PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit customer information.
    """
    permission_required = 'products.edit_customermodel'
    template_name = 'products/customers/customermodel_form.html'
    model = CustomerModel
    fields = '__all__'
    success_url = '/customer_list/'


class CustomerDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a customer info from database.
    """
    permission_required = 'products.delete_customermodel'
    template_name = 'products/customers/customermodel_confirm_delete.html'
    model = CustomerModel
    success_url = '/customer_list/'


class ProductListView(View):
    """
    Class display a list of all
    door lines available.
    """
    def get(self, request):
        door_list = ProductsModel.objects.all()
        return render(
            request,
            'products/doors/products_list.html',
            {'door_list': door_list}
        )


class ProductDetailView(View):
    """
    Class display detailed view of
    specific door.
    """
    def get(self, request, pk):
        try:
            door_detail = ProductsModel.objects.get(id=pk)
            return render(
                request,
                'products/doors/products_details.html',
                {'door_detail': door_detail}
            )
        except KeyError:
            return redirect('/door_list/')


class ProductAddView(PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new door line to database.
    """
    permission_required = 'products.add_productsmodel'
    template_name = 'products/doors/productsmodel_form.html'
    model = ProductsModel
    fields = '__all__'
    success_url = '/door_list/'


class ProductEditView(PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit door information.
    """
    permission_required = 'products.edit_productsmodel'
    template_name = 'products/doors/productsmodel_form.html'
    model = ProductsModel
    fields = '__all__'
    success_url = '/door_list/'


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Class deleting a door line from database.
    """
    permission_required = 'products.delete_productsmodel'
    template_name = 'products/doors/productsmodel_confirm_delete.html'
    model = ProductsModel
    success_url = '/door_list/'


class ScanProductionView(View):
    """
    class allowing to scan doors on shop floor
    on start and end of production on each
    production stage
    """
    def get(self, request):
        scan_in_form = ScanProductionForm()

        return render(
            request,
            'products/production/user_scanner_form.html',
            {'scan_in_form': scan_in_form}
        )

    def post(self, request):
        current_employee = EmployeeModel.objects.get(user=request.user)
        scan_filter = r'^(?P<prefix>job)(?P<order>\d{1,7})-(?P<job>\d{1,4})'
        # now = f'{datetime.now().strftime("%Y-%m-%d %H:%M")}'
        now = timezone.make_aware(datetime.now())
        print(now)
        # aware_start_time = timezone.make_aware(datetime.now())
        if 'start' in request.POST:
            full_number = re.match(
                scan_filter,
                request.POST['job_no'],
                flags=re.IGNORECASE,
            )
            prefix = full_number['prefix']
            ord_no = full_number['order']
            if len(ord_no) < 7:
                ord_no = ord_no.rjust(7, '0')
            job_no = full_number['job']
            if len(job_no) < 4:
                job_no = job_no.rjust(4, '0')

            try:
                order = OrderModel.objects.get(
                    order_number__icontains=prefix + ord_no
                )
            except ObjectDoesNotExist:
                return redirect(to='/scan_product/')

            try:
                job = ProductsModel.objects.get(
                    order_num=order,
                    job_no__icontains=job_no
                )
            except ObjectDoesNotExist:
                return redirect(to='/scan_product/')

            if not UserProductModel.objects.filter(
                    product_id=job,
                    user_id=current_employee,
            ):
                scan = UserProductModel.objects.create(
                    product_id=job,
                    user_id=current_employee,
                    prod_start=now,
                )
            else:
                scan = UserProductModel.objects.update(
                    product_id=job,
                    user_id=current_employee,
                    prod_start=now,
                )
            return redirect(to='/scan_product/')

        if 'finish' in request.POST:
            full_number = re.match(
                scan_filter,
                request.POST['job_no'],
                flags=re.IGNORECASE,
            )
            prefix = full_number['prefix']
            ord_no = full_number['order']
            if len(ord_no) < 7:
                ord_no = ord_no.rjust(7, '0')
            job_no = full_number['job']
            if len(job_no) < 4:
                job_no = job_no.rjust(4, '0')

            try:
                order = OrderModel.objects.get(
                    order_number__icontains=prefix + ord_no
                )
            except ObjectDoesNotExist:
                return redirect(to='/scan_product/')

            try:
                job = ProductsModel.objects.get(
                    order_num=order,
                    job_no__icontains=job_no
                )
            except ObjectDoesNotExist:
                return redirect(to='/scan_product/')

            if not UserProductModel.objects.filter(
                    product_id=job,
                    user_id=current_employee,
            ):
                scan = UserProductModel.objects.create(
                    product_id=job,
                    user_id=current_employee,
                    prod_end=now,
                )
            else:
                scan = UserProductModel.objects.update(
                    product_id=job,
                    user_id=current_employee,
                    prod_end=now,
                )
            return redirect(to='/scan_product/')

        else:
            return redirect(to='/scan_product/')


