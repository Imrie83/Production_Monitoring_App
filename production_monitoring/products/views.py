from datetime import datetime
from django.db.models import Q
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import PermissionRequiredMixin, \
    LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
import re

from admin_app.models import UserProductModel, EmployeeModel
from products.forms import (
    ComponentAddForm,
    ScanProductionForm,
    ComponentToolsForm,
    GlassAddForm,
    GlassToolAddForm,
    ProductAddForm,
    ProductEditForm,
    ProductComponentAddForm,
)
from products.models import (
    OrderModel,
    ProductsModel,
    ComponentsModel,
    CustomerModel,
    DoorStyleModel,
    GlassModel,
    ComponentToolsModel,
    GlassToolModel,
    ProductComponent,
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

    def post(self, request):
        if 'search' in request.POST:
            search_q = request.POST['search']
            orders = OrderModel.objects.filter(
                Q(order_number__icontains=search_q)
            ).order_by('order_number')
            return render(
                request,
                'products/orders/order_list.html',
                {'orders': orders}
            )


class OrderDetailView(LoginRequiredMixin, View):
    """
    Class display a detailed view of each order.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        try:
            order_details = OrderModel.objects.get(id=pk)
            order_list = OrderModel.objects.all()
            return render(
                request,
                'products/orders/order_details.html',
                {
                    'order_details': order_details,
                    'order_list': order_list,
                }
            )
        except KeyError:
            return redirect('/order_list/')

    def post(self, request, pk):
        if 'search' in request.POST:
            search_q = request.POST['search']
            orders = OrderModel.objects.filter(
                Q(order_number__icontains=search_q) |
                Q(customer_id__customer_name__icontains=search_q)
            ).order_by('order_number')
            return render(
                request,
                'products/orders/order_list.html',
                {'orders': orders}
            )


class EditOrderView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class allowing to edit order details.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.update_ordermodel'
    template_name = 'products/orders/ordermodel_form.html'
    model = OrderModel
    fields = '__all__'
    success_url = '/order_list/'


class DeleteOrderView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    class allowing to delete an order from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.delete_ordermodel'
    template_name = 'products/orders/ordermodel_confirm_delete.html'
    model = OrderModel
    success_url = '/order_list/'


class AddOrderView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class allowing to create a new order line.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.add_ordermodel'
    template_name = 'products/orders/ordermodel_form.html'
    model = OrderModel
    fields = '__all__'
    success_url = '/order_list/'


# TODO: clean duplicate code!
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

    def post(self, request):
        if 'search' in request.POST:
            search_q = request.POST['search']
            component_list = ComponentsModel.objects.filter(
                Q(name__icontains=search_q) |
                Q(door_type__icontains=search_q) |
                Q(product_type__icontains=search_q)
            ).order_by('name')
            return render(
                request,
                'products/components/component_list.html',
                {'component_list': component_list}
            )


class ComponentDetailView(LoginRequiredMixin, View):
    """
    Class displaying component details.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        try:
            component_list = ComponentsModel.objects.all()
            component_details = ComponentsModel.objects.get(id=pk)
            return render(
                request,
                'products/components/component_details.html',
                {
                    'component_details': component_details,
                    'component_list': component_list
                }
            )
        except KeyError:
            return redirect('/component_list/')

    def post(self, request, pk):
        if 'search' in request.POST:
            search_q = request.POST['search']
            component_list = ComponentsModel.objects.filter(
                Q(name__icontains=search_q) |
                Q(door_type__icontains=search_q) |
                Q(product_type__icontains=search_q)
            ).order_by('name')
            return render(
                request,
                'products/components/component_list.html',
                {'component_list': component_list}
            )


class AddComponentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class displaying form allowing to add a new component
    in to the database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.add_componentsmodel'

    def get(self, request):
        form = ComponentAddForm()
        return render(
            request,
            'products/components/componentsmodel_form.html',
            {'form': form}
        )

    def post(self, request):
        form = ComponentAddForm(request.POST)
        if form.is_valid():
            new_component = ComponentsModel.objects.create(
                name=form.cleaned_data['name'],
                stock=form.cleaned_data['stock'],
                door_type=form.cleaned_data['door_type'],
                product_type=form.cleaned_data['product_type'],
                component_description=form.cleaned_data[
                    'component_description'],
                img=form.cleaned_data['img']
            )
            return redirect(to=f'/component_details/{new_component.pk}')
        else:
            return render(
                request,
                'products/components/componentsmodel_form.html/',
                {'form': form}
            )


class AddComponentToolView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class creating a form allowing to
    add tools with machining times to each component.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'product.edit_componenttoolsmodel'

    def get(self, request, pk):
        form = ComponentToolsForm()
        return render(
            request,
            'products/components/componentsmodel_form.html',
            {'form': form}
        )

    def post(self, request, pk):
        form = ComponentToolsForm(request.POST)
        assign_to_comp = ComponentsModel.objects.get(id=pk)
        if form.is_valid():
            add_tool = ComponentToolsModel.objects.create(
                component_id=assign_to_comp,
                tools_id=form.cleaned_data['tools_id'],
                machine_time=form.cleaned_data['machine_time'],
            )
            return redirect(to=f'/component_details/{assign_to_comp.pk}')
        else:
            return render(
                request,
                'products/components/componentsmodel_form.html/',
                {'form': form}
            )


class EditComponentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display a form allowing to update information
    about a component.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.edit_componentsmodel'
    template_name = 'products/components/componentsmodel_form.html'
    model = ComponentsModel
    fields = '__all__'
    success_url = '/component_list/'


class DeleteComponentView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a component.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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

    def post(self, request):
        if 'search' in request.POST:
            search_q = request.POST['search']
            glass_list = GlassModel.objects.filter(
                Q(glass_name__icontains=search_q) |
                Q(glass_door_type__icontains=search_q)
            ).order_by('glass_name')
            return render(
                request,
                'products/glass/glass_list.html',
                {'glass_list': glass_list}
            )


class GlassDetailView(LoginRequiredMixin, View):
    """
    Class display detailed view of
    specific glass.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        glass_list = GlassModel.objects.all()
        try:
            glass_detail = GlassModel.objects.get(id=pk)
            return render(
                request,
                'products/glass/glass_details.html',
                {
                    'glass_detail': glass_detail,
                    'glass_list': glass_list,
                 }
            )
        except KeyError:
            return redirect('/glass_list/')

    def post(self, request, pk):
        if 'search' in request.POST:
            search_q = request.POST['search']
            glass_list = GlassModel.objects.filter(
                Q(glass_name__icontains=search_q) |
                Q(glass_door_type__icontains=search_q)
            ).order_by('glass_name')
            return render(
                request,
                'products/glass/glass_list.html',
                {'glass_list': glass_list}
            )


class GlassAddView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class displaying a form allowing
    to add a new piece of glass  to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.add_glassmodel'

    def get(self, request):
        form = GlassAddForm
        return render(
            request,
            'products/glass/glassmodel_form.html',
            {'form': form}
        )

    def post(self, request):
        form = GlassAddForm(request.POST)
        if form.is_valid():
            new_glass = GlassModel.objects.create(
                glass_name=form.cleaned_data['glass_name'],
                glass_door_type=form.cleaned_data['glass_door_type'],
                stock=form.cleaned_data['stock'],
                description=form.cleaned_data['description'],
                img=form.cleaned_data['img'],
            )
            return redirect(to=f'/glass_detail/{new_glass.pk}/')
        else:
            return render(
                request,
                'products/glass/glassmodel_form.html',
                {'form': form},
            )


class GlassToolAddView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class display a form allowing to
    add tool and machining time to a piece
    of glass.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.add_glasstoolmodel'

    def get(self, request, pk):
        form = GlassToolAddForm()
        return render(
            request,
            'products/glass/glassmodel_form.html',
            {'form': form}
        )

    def post(self, request, pk):
        form = GlassToolAddForm(request.POST)
        assign_to_glass = GlassModel.objects.get(id=pk)
        if form.is_valid():
            new_glass_too = GlassToolModel.objects.create(
                glass_id=assign_to_glass,
                tool_id=form.cleaned_data['tool_id'],
                machine_time=form.cleaned_data['machine_time'],
            )
            return redirect(to=f'/glass_detail/{assign_to_glass.pk}/')
        else:
            return render(
                request,
                'products/glass/glassmodel_form.html',
                {'form': form}
            )


class GlassEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit glass information.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.edit_glassmodel'
    template_name = 'products/glass/glassmodel_form.html'
    model = GlassModel
    fields = '__all__'
    success_url = '/glass_list/'


class GlassDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a piece of glass from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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


class StyleDetailView(LoginRequiredMixin, View):
    """
    Class display detailed view of
    specific door style.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

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


class StyleAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new door style to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.add_doorstylemodel'
    template_name = 'products/styles/doorstylemodel_form.html'
    model = DoorStyleModel
    fields = '__all__'
    success_url = '/style_list/'


class StyleEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit style information.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.edit_doorstylemodel'
    template_name = 'products/styles/doorstylemodel_form.html'
    model = DoorStyleModel
    fields = '__all__'
    success_url = '/style_list/'


class StyleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a door style from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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


class CustomerDetailView(LoginRequiredMixin, View):
    """
    Class display detailed view of
    specific customer.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        customer_list = CustomerModel.objects.all()
        try:
            customer_detail = CustomerModel.objects.get(id=pk)
            return render(
                request,
                'products/customers/customer_details.html',
                {
                    'customer_detail': customer_detail,
                    'customer_list': customer_list,
                }
            )
        except KeyError:
            return redirect('/customer_list/')


class CustomerAddView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Class displaying a form allowing
    to add a new customer to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.add_customermodel'
    template_name = 'products/customers/customermodel_form.html'
    model = CustomerModel
    fields = '__all__'
    success_url = '/customer_list/'


class CustomerEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit customer information.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.edit_customermodel'
    template_name = 'products/customers/customermodel_form.html'
    model = CustomerModel
    fields = '__all__'
    success_url = '/customer_list/'


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a customer info from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
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
        door_list = ProductsModel.objects.all().order_by(
            'order_num',
            'job_no',
        )

        return render(
            request,
            'products/doors/products_list.html',
            {'door_list': door_list}
        )

    def post(self, request):
        if 'search' in request.POST:
            search_q = request.POST['search']
            door_list = ProductsModel.objects.filter(
                Q(job_no__icontains=search_q) |
                Q(order_num__order_number__icontains=search_q) |
                Q(door_type__icontains=search_q) |
                Q(delivery_date__icontains=search_q) |
                Q(production_date__icontains=search_q) |
                Q(delivery_address__icontains=search_q) |
                Q(finished__icontains=search_q)
            ).order_by('order_num', 'job_no')

            return render(
                request,
                'products/doors/products_list.html',
                {'door_list': door_list}
            )


class ProductDetailView(LoginRequiredMixin, View):
    """
    Class display detailed view of
    specific door.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        order = OrderModel.objects.get(product=pk)
        product_list = ProductsModel.objects.filter(order_num_id=order).order_by(
            'order_num',
            'job_no',
        )
        try:
            door_detail = ProductsModel.objects.get(id=pk)
            return render(
                request,
                'products/doors/products_details.html',
                {
                    'door_detail': door_detail,
                    'door_list': product_list,
                }
            )
        except KeyError:
            return redirect('/door_list/')


class ProductAddView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class displaying a form allowing
    to add a new door line to database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    permission_required = 'products.add_productsmodel'

    def get(self, request):
        form = ProductAddForm()
        return render(
            request,
            'products/doors/productsmodel_form.html',
            {'form': form}
        )

    def post(self, request):
        form = ProductAddForm(request.POST)
        if form.is_valid():
            new_door = ProductsModel.objects.create(
                order_num=form.cleaned_data['order_num'],
                job_no=form.cleaned_data['job_no'],
                door_type=form.cleaned_data['door_type'],
                color=form.cleaned_data['color'],
                style=form.cleaned_data['style'],
                glass=form.cleaned_data['glass'],
                handing=form.cleaned_data['handing'],
                door_width=form.cleaned_data['door_width'],
                door_height=form.cleaned_data['door_height'],
                trim_with=form.cleaned_data['trim_with'],
                delivery_date=form.cleaned_data['delivery_date'],
                delivery_address=form.cleaned_data['delivery_address'],
                production_date=form.cleaned_data['production_date'],
            )

            glass = GlassModel.objects.get(id=new_door.glass.pk)
            if glass.stock > 0:
                glass.stock -= 1
                glass.save()

            return redirect(f'/door_details/{new_door.pk}/')
        else:
            return render(
                request,
                'products/doors/productsmodel_form.html',
                {'form': form}
            )


class ProductComponentAddView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Class create view displaying form
    allowing to add components to each door.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.edit_productsmodel'

    def get(self, request, pk):
        form = ProductComponentAddForm()
        return render(
            request,
            'products/doors/productsmodel_form.html',
            {'form': form}
        )

    def post(self, request, pk):
        form = ProductComponentAddForm(request.POST)
        product = ProductsModel.objects.get(id=pk)

        if form.is_valid():
            add_comp = ProductComponent.objects.create(
                product_id=product,
                component_id=form.cleaned_data['component_id'],
                count=form.cleaned_data['count'],
            )
            component = form.cleaned_data['component_id']

            if component.stock > 0:
                component.stock -= form.cleaned_data['count']
                component.save()

            return redirect(f'/door_details/{product.id}/')
        else:
            return render(
                request,
                'products/doors/productsmodel_form.html',
                {'form': form}
            )


class ProductEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Class display form view allowing to edit door information.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.edit_productsmodel'
    template_name = 'products/doors/productsmodel_form.html'
    model = ProductsModel
    # fields = '__all__'
    form_class = ProductEditForm
    success_url = '/door_list/'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Class deleting a door line from database.
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'
    permission_required = 'products.delete_productsmodel'
    template_name = 'products/doors/productsmodel_confirm_delete.html'
    model = ProductsModel
    success_url = '/door_list/'


class ScanProductionView(LoginRequiredMixin, View):
    """
    class allowing to scan doors on shop floor
    on start and end of production on each
    production stage
    """
    login_url = '/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        scan_in_form = ScanProductionForm()

        return render(
            request,
            'products/production/user_scanner_form.html',
            {'scan_in_form': scan_in_form}
        )

    # TODO: set error messages for the operator!
    # TODO: refactor - shorten the repeated code!
    def post(self, request):
        current_employee = EmployeeModel.objects.get(user=request.user)
        user_departments = []

        # TODO: add output to scanner
        # now = datetime.now().strftime('%Y-%m-%d')
        # my_output = UserProductModel.objects.filter(
        #     user_id=current_employee,
        #     prod_end__icontains=now,
        # )

        for key, value in list(current_employee.section_id.values_list()):
            user_departments.append(value)

        scan_filter = r'^(?P<prefix>job)(?P<order>\d{1,7})-(?P<job>\d{1,4})'
        now = timezone.make_aware(datetime.now())
        scan_in_form = ScanProductionForm(request.POST)
        if scan_in_form.is_valid():
            job_scan = scan_in_form.cleaned_data['job_no']

            if 'start' in request.POST:
                full_number = re.match(
                    scan_filter,
                    job_scan,
                    flags=re.IGNORECASE,
                )
                prefix = full_number['prefix'].upper()
                ord_no = full_number['order']
                if len(ord_no) < 7:
                    ord_no = ord_no.rjust(7, '0')
                job_no = full_number['job']
                if len(job_no) < 4:
                    job_no = job_no.rjust(4, '0')

                try:
                    order = OrderModel.objects.get(
                        order_number=prefix + ord_no
                    )
                except ObjectDoesNotExist:
                    return render(
                        request,
                        'products/production/user_scanner_form.html',
                        {
                            'scan_in_form': scan_in_form,
                            'error': 'Order Does Not Exist',
                            'my_output': my_output,
                        }
                    )

                try:
                    job = ProductsModel.objects.get(
                        order_num=order,
                        job_no=job_no
                    )
                except ObjectDoesNotExist:
                    return render(
                        request,
                        'products/production/user_scanner_form.html',
                        {
                            'scan_in_form': scan_in_form,
                            'error': 'Job Does Not Exist',
                            'my_output': my_output,
                        }
                    )

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
                    update_scan = UserProductModel.objects.get(
                        product_id=job,
                        user_id=current_employee,
                    )
                    update_scan.prod_start = now
                    update_scan.save()

                return redirect(to='/scan_product/')

            if 'finish' in request.POST:
                full_number = re.match(
                    scan_filter,
                    job_scan,
                    flags=re.IGNORECASE,
                )
                prefix = full_number['prefix'].upper()
                ord_no = full_number['order']
                if len(ord_no) < 7:
                    ord_no = ord_no.rjust(7, '0')
                job_no = full_number['job']
                if len(job_no) < 4:
                    job_no = job_no.rjust(4, '0')

                try:
                    order = OrderModel.objects.get(
                        order_number=prefix + ord_no
                    )
                except ObjectDoesNotExist:
                    return render(
                        request,
                        'products/production/user_scanner_form.html',
                        {
                            'scan_in_form': scan_in_form,
                            'error': 'Order Does Not Exist'
                        }
                    )

                try:
                    job = ProductsModel.objects.get(
                        order_num=order,
                        job_no=job_no
                    )
                except ObjectDoesNotExist:
                    return render(
                        request,
                        'products/production/user_scanner_form.html',
                        {
                            'scan_in_form': scan_in_form,
                            'error': 'Job Does Not Exist'
                        }
                    )

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
                    update_scan = UserProductModel.objects.get(
                        product_id=job,
                        user_id=current_employee,
                    )
                    update_scan.prod_end = now
                    update_scan.save()

                if 'Packing' in user_departments:
                    job.finished = True
                    job.save()
                    return redirect(to='/scan_product/')

                for comp in ProductComponent.objects.filter(product_id=job):

                    if 'CNC' in user_departments:
                        # TODO: sort out duplicate code!
                        for tool in comp.component_id.tools_req.all():
                            try:

                                if tool.current_run_time >= tool.max_run_time:
                                    tool.current_run_time = (
                                            tool.current_run_time - tool.max_run_time
                                    )
                                    tool.stock -= 1
                                    if tool.stock < 0:
                                        tool.stock = 0
                                tool.save()
                                # TODO: sort out exception handling
                            except ObjectDoesNotExist:
                                return redirect('/scan_product/')
                            except AttributeError:
                                return redirect('/scan_product/')

                        glass = GlassToolModel.objects.filter(glass_id=job.glass.pk)

                        for tools in glass:
                            try:
                                tool = tools.tool_id
                                tool.current_run_time += tools.machine_time
                                if tool.current_run_time >= tool.max_run_time:
                                    tool.current_run_time = (
                                            tool.current_run_time - tool.max_run_time
                                    )
                                    tool.stock -= 1
                                    if tool.stock < 0:
                                        tool.stock = 0
                                tool.save()
                            except ObjectDoesNotExist:
                                return redirect('/scan_product/')
                            except AttributeError:
                                return redirect('/scan_product/')

                        door_trim_time = (
                                ((job.door_height * 2) + (job.door_width * 2))
                                / 1000 / job.trim_with.feed_rate
                        )
                        door_trim_tool = job.trim_with
                        door_trim_tool.current_run_time += door_trim_time
                        if door_trim_tool.current_run_time >= door_trim_tool.max_run_time:
                            door_trim_tool.current_run_time = (
                                    door_trim_tool.current_run_time - door_trim_tool.max_run_time
                            )
                            door_trim_tool.stock -= 1
                            if door_trim_tool.stock < 0:
                                door_trim_tool.stock = 0

                        door_trim_tool.save()

                        return redirect(to='/scan_product/')
                    else:
                        return redirect(to='/scan_product/')
                else:
                    return redirect(to='/scan_product/')
        else:
            return redirect(to='/scan_product/')
