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
]
