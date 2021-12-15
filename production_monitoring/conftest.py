import pytest
from django.contrib.auth.models import User, Group
from datetime import datetime
from admin_app.models import (
    EmployeeModel,
    UserProductModel,
)

from products.models import (
    ProductsModel,
    OrderModel,
    CustomerModel,
    DoorStyleModel,
    GlassModel,
)

from tools.models import ToolsModel


@pytest.fixture
def create_test_tool():
    """
    Function creates a dummy tool.
    :return: ToolModel object.
    """
    return [ToolsModel.objects.create(
        tool_name='Turbo Cutter',
        feed_rate=5,
        type='PCD',
        stock=10,
        max_run_time=600,
        description='Lorem ipsum dolor set',
        current_run_time=10,
    ),
        ToolsModel.objects.create(
            tool_name='Rough Cutter',
            feed_rate=5,
            type='Carbide',
            stock=10,
            max_run_time=600,
            description='Lorem ipsum dolor set',
            current_run_time=10,
        )]


@pytest.fixture
def test_customer():
    """
    Create a CustomerModel object.
    :return: customer
    """
    customer = CustomerModel.objects.create(
        customer_name='Safestyle',
        customer_email='info@safestyle.co.uk',
        customer_phone='07877884534',
    )
    return customer


@pytest.fixture
def test_order(test_customer):
    """
    Create OrderModel object.
    :param test_customer:
    :return: order
    """
    order = OrderModel.objects.create(
        order_number='JOB0000001',
        customer_id=test_customer,
    )
    return order


@pytest.fixture
def test_style():
    """
    create DoorStyleModel objects.
    :return: style
    """
    style = DoorStyleModel.objects.create(
        style_name='Gloucester',
    )
    return style


@pytest.fixture
def test_glass():
    """
    Create GlassModel object.
    :return: glass
    """
    glass = GlassModel.objects.create(
        glass_name='Gloucester',
        glass_door_type='firedoor',
    )
    return glass


@pytest.fixture
def test_product(test_order, test_style, test_glass, create_test_tool):
    """
    Create a ProductsModel object.

    :param test_order:
    :param test_style:
    :param test_glass:
    :param create_test_tool:
    :return: product
    """
    now = datetime.now().strftime('%Y-%m-%d')
    product = ProductsModel.objects.create(
        order_num=test_order,
        job_no='0001',
        door_type='firedoor',
        color='white',
        style=test_style,
        glass=test_glass,
        handing='LI',
        door_width=800,
        door_height=1984,
        trim_with=create_test_tool[0],
        production_date=now,
    )
    return product


@pytest.fixture
def test_groups():
    """
    Create a list of groups available for users.
    :return: groups
    """
    group_1 = Group.objects.create(
        name='Manager'
    )
    group_2 = Group.objects.create(
        name='Shop floor staff'
    )
    group_3 = Group.objects.create(
        name='Supervisor'
    )
    groups = Group.objects.all()
    return groups


@pytest.fixture
def test_user(test_groups):
    """
    A fixture creating a default user and employee
    belonging to all groups.
    Allows testing access to all section of the app

    :return: User object.
    """
    default_user = User.objects.create(
        username='imrie',
        is_superuser=True,
        password='test123test',
        is_active=True,
        is_staff=True,
    )
    default_user.groups.set(test_groups)
    # default_user.user_permissions.add()
    return default_user


@pytest.fixture
def test_employee(test_user):
    """
    Create an EmployeeModel object.
    :param test_user:
    :return: default_employee
    """
    default_employee = EmployeeModel.objects.create(
        user_id=test_user.pk,
        id_num=666,
    )
    return default_employee


@pytest.fixture
def test_user_product(test_product, test_employee):
    """
    Create and entry in UserProduct model.

    :param test_product:
    :param test_employee:
    :return: user_product
    """
    now = datetime.now().strftime('%Y-%m-%d')
    user_product = UserProductModel.objects.create(
        user_id=test_employee,
        product_id=test_product,
        prod_end=now,
    )
    return user_product
