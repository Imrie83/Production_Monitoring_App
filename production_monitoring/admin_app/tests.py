import pytest
from django.contrib import auth
from django.contrib.auth.models import User


# TODO: sort out log in test -> currently password not passed in context?
# @pytest.mark.django_db
# def test_login_page(client, test_user):
#     """
#     Function test displaying a login page
#     and user log in function.
#
#     :param client:
#     :param test_user:
#     """
#     # check if user in database
#     assert User.objects.get(username='imrie').username == 'imrie'
#     assert User.objects.get(username='imrie').password == 'test123test'
#
#     response = client.get('/login/')
#     assert response.status_code == 200
#
#     # try to login existing user
#     response = client.post('/login/', {
#         'login': 'imrie',
#         'password': 'test123test',  # <- password not passed in context?
#         }
#     )
#
#     print(response.context)
#     assert response.status_code == 302


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
