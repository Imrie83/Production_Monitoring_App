import pytest
from django.contrib.auth.models import User, Group

from tools.models import ToolsModel


@pytest.fixture
def create_test_tool():
    """
    Function creates a dummy tool.
    :return: ToolModel object.
    """
    return ToolsModel.objects.create(
        tool_name='Turbo Cutter',
        feed_rate=5,
        type='PCD',
        stock=10,
        max_run_time=600,
        description='Lorem ipsum dolor set',
        current_run_time=10,
    )


@pytest.fixture
def test_user():
    """
    A fixture creating a default user
    belonging to all groups.
    Allows testing access to all section of the app

    :return: User object.
    """
    # groups = Group.objects.all()
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

    default_user = User.objects.create(
        username='imrie',
        is_superuser=True,
        password='test123test',
        is_active=True,
        is_staff=True,
    )
    default_user.groups.set(groups)
    return default_user
