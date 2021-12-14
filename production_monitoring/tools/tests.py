import pytest
from django.contrib import auth
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_login_page(client, test_user):
    """
    Function test displaying a login page
    and user log in function.

    :param client:
    :param test_user:
    """
    response = client.get('')
    assert response.status_code == 200

    response = client.post('', {'username': 'imrie', 'password': 'test123test'})
    user = User.objects.get(username='imrie')
    assert response.status_code == 200
    assert user.is_authenticated


@pytest.mark.django_db
def test_tool_detail(client, test_user, create_test_tool):
    """
    Function test if tool details and tool list load correctly.

    :param client:
    :param test_user:
    :param create_test_tool:
    """
    response = client.get(f'/tool_details/{create_test_tool[0].pk}/')
    tool = response.context['tool_details']
    tool_list = response.context['tool_list']
    assert response.status_code == 200
    assert tool.tool_name == 'Turbo Cutter'
    assert tool.feed_rate == 5
    assert tool.type == 'PCD'
    assert tool.stock == 10
    assert tool.max_run_time == 600
    assert tool.description == 'Lorem ipsum dolor set'
    assert tool.current_run_time == 10
    assert len(tool_list) == 2


# @pytest.mark.django_db
# def test_product_page(client, example_product):
#     response = client.get(f'/product/{example_product.id}/')
#     assert response.status_code == 200
#     assert response.context['description'] == 'Example Test Description'
#     assert response.context['name'] == 'product'
#     assert response.context['price'] == 356
#
#
# @pytest.mark.django_db
# def test_product_addition(client):
#     response = client.post('/product/add/',
#                            {'name': 'a test product',
#                             'description': 'a test description', 'price': 500})
#     product = Product.objects.get(name='a test product')
#     assert response.status_code == 302
#     assert product.description == 'a test description'
#     assert product.price == 500