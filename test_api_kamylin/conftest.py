import pytest
from endpoints.create_obj import CreateObj
from endpoints.get_obj import GetObject
from endpoints.delete_obj import DeleteObj
from endpoints.put_obj import PutObj
from endpoints.patch_obj import PatchObject


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
