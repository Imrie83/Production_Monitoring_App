"""production_monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from tools.views import (
    AddToolView,
    ToolListView,
    EditToolView,
    DeleteToolView,
    ToolDetailsView,
)

from products.views import (
    OrderListView,
    OrderDetailView,
    AddOrderView,
    EditOrderView,
    DeleteOrderView,
    ComponentListView,
    ComponentDetailView,
    AddComponentView,
    EditComponentView,
    DeleteComponentView,
    GlassListView,
    GlassDetailView,
    GlassAddView,
    GlassEditView,
    GlassDeleteView,
    StyleListView,
    StyleDetailView,
    StyleAddView,
    StyleEditView,
    StyleDeleteView,
    CustomerListView,
    CustomerDetailView,
    CustomerAddView,
    CustomerEditView,
    CustomerDeleteView,
)

from admin_app.views import (
    LoginView,
    PanelView,
    LogoutView,
)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('panel/', PanelView.as_view(), name='panel'),

    path('tool_list/', ToolListView.as_view(), name='tools'),
    path('add_tools/', AddToolView.as_view(), name='add_tools'),
    path('edit_tool/<int:pk>/', EditToolView.as_view(), name='edit_tool'),
    path('delete_tool/<int:pk>/', DeleteToolView.as_view(), name='delete_tool'),
    path('tool_details/<int:pk>/', ToolDetailsView.as_view()),

    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('order_details/<int:pk>/', OrderDetailView.as_view()),
    path('add_order/', AddOrderView.as_view(), name='add_order'),
    path('edit_order/<int:pk>/', EditOrderView.as_view(), name='edit_order'),
    path('delete_order/<int:pk>/', DeleteOrderView.as_view(), name='delete_order'),

    path('component_list/', ComponentListView.as_view(), name='component_list'),
    path('component_details/<int:pk>/', ComponentDetailView.as_view()),
    path('add_component/', AddComponentView.as_view(), name='add_component'),
    path('edit_component/<int:pk>/', EditComponentView.as_view(), name='edit_component'),
    path('delete_component/<int:pk>/', DeleteComponentView.as_view(), name='delete_component'),

    path('glass_list/', GlassListView.as_view(), name='glass_list'),
    path('glass_detail/<int:pk>/', GlassDetailView.as_view(), name='glass_detail'),
    path('add_glass/', GlassAddView.as_view(), name='add_glass'),
    path('edit_glass/<int:pk>/', GlassEditView.as_view(), name='edit_glass'),
    path('delete_glass/<int:pk>/', GlassDeleteView.as_view(), name='delete_glass'),

    path('style_list/', StyleListView.as_view(), name='style_list'),
    path('style_details/<int:pk>/', StyleDetailView.as_view(), name='style_detail'),
    path('add_style/', StyleAddView.as_view(), name='add_style'),
    path('edit_style/<int:pk>/', StyleEditView.as_view(), name='edit_style'),
    path('delete_style/<int:pk>/', StyleDeleteView.as_view(), name='delete_style'),

    path('customer_list/', CustomerListView.as_view(), name='customer_list'),
    path('customer_details/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('add_customer/', CustomerAddView.as_view(), name='add_customer'),
    path('edit_customer/<int:pk>/', CustomerEditView.as_view(), name='edit_customer'),
    path('delete_customer/<int:pk>/', CustomerDeleteView.as_view(), name='delete_customer'),

]
