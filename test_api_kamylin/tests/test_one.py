import pytest
from endpoints.endpoint import Endpoint

test_data_1 = {
    'data': {'color': 'pink', 'size': 'middle'},
    'name': 'Chebyx'
}

test_data_2 = [
    {'data': {'color': 'pink', 'size': 'middle'}, 'name': 'Chebyx'},
    {'data': {'color': 'green', 'size': 'big'}, 'name': 'Rabbit'},
    {'data': {'color': 'grey', 'size': 'smole'}, 'name': 'Hot'}
]


@pytest.mark.parametrize('data', test_data_2)
def test_creation_object(create_object, data):
    create_object.create(data)
    create_object.check_status_code()


def test_get_all_object(get_obj):
    get_obj.test_all_object()
    get_obj.check_status_code()


def test_get_one_object(create_data, get_obj):
    get_obj.test_one_object(create_data)
    get_obj.check_response_id(create_data)


def test_put_object(create_data, put_obj):
    payload = {
        'data': {'color': 'blue', 'size': 'very big'},
        'name': 'Chicken'
    }
    put_obj.change_object(create_data, payload)
    put_obj.check_status_code()


def test_patch_object(create_data, patch_obj):
    payload = payload = {'name': 'Bulka'}
    patch_obj.change_patch_object(create_data, payload)
    patch_obj.check_update_data(payload['name'])


def test_delete_object(create_data_for_del, del_obj):
    del_obj.delete_obj(create_data_for_del)
    del_obj.check_status_code()
