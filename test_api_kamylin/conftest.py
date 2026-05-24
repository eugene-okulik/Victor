import pytest
import requests
from endpoints.create_obj import CreateObj
from endpoints.get_obj import GetObject
from endpoints.delete_obj import DeleteObj
from endpoints.put_obj import PutObj
from endpoints.patch_obj import PatchObject
from endpoints.endpoint import Endpoint


@pytest.fixture()
def create_object():
    return CreateObj()


@pytest.fixture()
def get_obj():
    return GetObject()


@pytest.fixture()
def put_obj():
    return PutObj()


@pytest.fixture()
def patch_obj():
    return PatchObject()


@pytest.fixture()
def del_obj():
    return DeleteObj()


@pytest.fixture
def create_data(create_object):
    payload = {
        'data': {'color': 'RED', 'size': 'middle'},
        'name': 'Malina'
    }
    create_object.create(payload)
    yield create_object.object_id
    if create_object.object_id:
        requests.delete(f'{create_object.url}/{create_object.object_id}')


@pytest.fixture
def create_data_for_del(create_object):
    payload = {
        'data': {'color': 'RED', 'size': 'middle'},
        'name': 'Dog'
    }
    create_object.create(payload)
    yield create_object.object_id
