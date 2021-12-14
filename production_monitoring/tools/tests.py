import pytest
from django.contrib import auth
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_login_page(client, test_user):
    response = client.get('')
    assert response.status_code == 200

    response = client.post('', {'username': 'imrie', 'password': 'test123test'})
    user = User.objects.get(username='imrie')
    assert response.status_code == 200
    assert user.is_authenticated


# @pytest.mark.django_db
# def test_tool_detail(client, test_user, create_test_tool):
#     user = User.objects.get(username='imrie')
#     client.login(username='imrie', password='test123test')
#     response = client.get(f'/tool_details/{create_test_tool.pk}/')
#     # assert response.status_code == 200
#     # assert response.context['tool_name'] == 'Turbo Cutter'


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