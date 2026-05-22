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


def test_get_one_object(create_object, get_obj):
    create_object.create(body=test_data_1)
    create_object.check_status_code()
    get_obj.test_one_object(create_object.object_id)
    get_obj.check_response_id(create_object.object_id)


def test_put_object(create_object, put_obj):
    payload = {
        'data': {'color': 'blue', 'size': 'very big'},
        'name': 'Chicken'
    }
    create_object.create(body=test_data_1)
    put_obj.change_object(create_object.object_id, payload)
    put_obj.check_status_code()


def test_patch_object(create_object, patch_obj):
    payload = payload = {'name': 'Bulka'}
    create_object.create(body=test_data_1)
    patch_obj.change_patch_object(create_object.object_id, payload)
    patch_obj.check_update_data(payload['name'])


def test_delete_object(create_object, del_obj):
    create_object.create(body=test_data_1)
    create_object.check_status_code()
    del_obj.delete_obj(create_object.object_id)
    del_obj.check_status_code
