import pytest
from django.contrib import auth
from django.contrib.auth.models import User

from admin_app.models import UserProductModel


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


# TODO: check if user actually logged out!
@pytest.mark.django_db
def test_logout_page(client, test_user):
    """
    function test if logout view redirects correctly.
    :param client:
    :param test_user:
    """
    response = client.get('/logout/')
    assert '/' in response.url
    assert response.status_code == 302


@pytest.mark.django_db
def test_panel_view(client, test_user, test_employee, test_product):
    user = client.force_login(test_user)
    response = client.get('/panel/')
    assert response.status_code == 200
    assert len(response.context['output']) == 0
    user_product = UserProductModel.objects.create(
        user_id=test_employee,
        product_id=test_product,
    )
