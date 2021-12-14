import pytest

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