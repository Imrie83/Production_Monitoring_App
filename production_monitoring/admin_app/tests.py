from datetime import datetime

import pytest
from django.contrib import auth
from django.contrib.auth.models import User


# TODO: finish this!
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
    response = client.post('', {'login': 'imrie', 'password': 'test123test'})
    # assert auth.get_user(client) == 'imrie'
    # assert response.status_code == 302


@pytest.mark.django_db
def test_logout_page(client, test_user):
    """
    function test if logout view redirects correctly.
    :param client:
    :param test_user:
    """
    user = client.force_login(test_user)
    assert auth.get_user(client).username == 'imrie'  # True -check if logged in
    response = client.get('/logout/')  # log out
    assert auth.get_user(client).username == ''  # True -check if user logged out
    assert '/' in response.url
    assert response.status_code == 302
