import pytest


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


@pytest.mark.django_db
def test_tool_list(client,  test_user, create_test_tool):
    """
    Function test if Toollist view is displayed correctly.

    :param client:
    :param test_user:
    :param create_test_tool:
    :return:
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

    # searching for type PCD
    response = client.post('/tool_list/', {'search': 'PCD'})
    tool_search = response.context['tool_list']
    assert response.status_code == 200
    assert len(response.context['tool_list']) == 1
    for tool in tool_search:
        assert 'PCD' in tool.type


# @pytest.mark.django_db
# def test_tool_add(client, test_user):
#     response = client.get('/add_tool/')
#     assert '/add_tool/' in response.url
#     response = client.post('/add_tool/',
#                            {
#                                'tool_name': 'V-point',
#                                'feed_rate': 10,
#                                'type': 'HSS',
#                                'stock': '20',
#                                'max_run_time': 500,
#                                'current_run_time': 0,
#                             }
#                            )
#     assert ToolsModel.objects.latest().tool_name == 'V-point'
