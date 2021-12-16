from datetime import datetime

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
    assert User.objects.get(username='staff').username == 'staff'
    assert User.objects.get(username='staff').password == 'staff'

    response = client.get('/')
    assert response.status_code == 200

    # TODO: make this work!
    response = client.post('', {'login': 'staff', 'password': 'staff'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_logout_page(client, test_user):
    """
    function test if logout view redirects correctly.
    :param client:
    :param test_user:
    """
    user = client.force_login(test_user[0])
    assert auth.get_user(client).username == 'imrie'  # True -check if logged in
    response = client.get('/logout/')  # log out
    assert auth.get_user(client).username == ''  # True -check if user logged out
    assert '/' in response.url
    assert response.status_code == 302
