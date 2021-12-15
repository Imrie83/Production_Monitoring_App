import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from tools.models import ToolsModel


@pytest.mark.django_db
def test_tool_detail(client, test_user, create_test_tool):
    """
    Function test if tool details and tool list load correctly.

    :param client:
    :param test_user:
    :param create_test_tool:
    """
    client.force_login(test_user)  # view restricted to logged in users!
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


@pytest.mark.django_db
def test_tool_list(client,  test_user, create_test_tool):
    """
    Function test if ToolList view is displayed correctly.

    :param client:
    :param test_user:
    :param create_test_tool:
    """
    response = client.get('/tool_list/')
    tool_list = response.context['tool_list']
    tools = []
    for tool in tool_list:
        tools.append(tool.tool_name)
    assert 'Turbo Cutter' in tools
    assert 'Rough Cutter' in tools
    assert len(tool_list) == 2
    assert response.status_code == 200

    # searching for tool_name 'Turbo Cutter
    response = client.post('/tool_list/', {'search': 'Turbo Cutter'})
    tool_search = response.context['tool_list']
    assert response.status_code == 200
    assert len(response.context['tool_list']) == 1
    for tool in tool_search:
        assert 'Turbo Cutter' in tool.tool_name
        assert 'Rough Cutter' not in tool.tool_name

    # searching for type PCD
    response = client.post('/tool_list/', {'search': 'PCD'})
    tool_search = response.context['tool_list']
    assert response.status_code == 200
    assert len(response.context['tool_list']) == 1
    for tool in tool_search:
        assert 'PCD' in tool.type
        assert 'Carbide' not in tool.type


@pytest.mark.django_db
def test_tool_add(client, test_user):
    """
    Function test if ToolAddView creates a new ToolModel object
    and save it to databasee.
    :param client:
    :param test_user:
    """
    response = client.get('/add_tool/')

    # No user logged in -> redirect to login page
    assert response.status_code == 302

    client.force_login(test_user)
    response = client.get('/add_tool/')

    # Gain access after login
    assert response.status_code == 200

    # test_image_2 = SimpleUploadedFile(
    #     name='16mm_rough.jpg',
    #     content=open('static/img/tools/16mm_rough.jpg', 'rb').read(), content_type='image/jpeg')

    test_image = SimpleUploadedFile("16mm_rough.jpg", b'file_cone', content_type="image/jpeg")
    print(test_image)
    print(type(test_image.name))
    # TODO: figure out a way to add image while creating the object in DB
    response = client.post('/add_tool/',
                           {
                               'tool_name': 'V-point',
                               'feed_rate': 10,
                               'type': 'HSS',
                               'stock': '20',
                               'max_run_time': 500,
                               'current_run_time': 0,
                               'image': test_image.name,
                            }
                           )
    assert response.status_code == 302  # redirect if tool added correctly
    tool = ToolsModel.objects.last()
    # tool.image = test_image  # add image to existing object
    assert tool.image == '16mm_rough.jpg'  # test if image exist
    assert tool.tool_name == 'V-point'
    assert response.status_code == 302  # redirect if tool added correctly


@pytest.mark.django_db
def test_tool_delete(client, test_user, create_test_tool):
    """
    function tests if tool deleted from database.

    :param client:
    :param test_user:
    :param create_test_tool:
    """
    client.force_login(test_user)
    tools = ToolsModel.objects.all()
    tool_1 = tools[0]
    # check tools in database
    assert tool_1.tool_name == 'Turbo Cutter'
    assert len(tools) == 2

    # delete tool
    response = client.post(f'/delete_tool/{tool_1.pk}/')

    # check redirection response code
    assert response.status_code == 302
    tools_2 = ToolsModel.objects.all()
    tool_2 = tools_2[0]

    # check if tools in database changed
    assert len(tools_2) == 1
    assert tool_2.tool_name != 'Turbo Cutter'


# @pytest.mark.django_db
# def test_tool_edit(client, test_user, create_test_tool):
#     client.force_login(test_user)
#     old_tool = create_test_tool[0]
#     response = client.get(f'/edit_tool/{old_tool.pk}/')
#     assert response.status_code == 200
#     assert b'Turbo Cutter' in response.content
#
#     response = client.post(
#         f'/edit_tool/{old_tool.pk}/',
#         {
#             'tool_name': 'Test Name',
#             'feed_rate': 55,
#             'type': 'HSS',
#             'in_stock': 10,
#             'allowed_run_time': 450,
#             'description': 'Lorem Ipsum',
#             # 'img': '',
#         }
#     )
#
#     assert response.status_code == 302

