import requests
import pytest


@pytest.fixture()
def create():
    body = {
        'data': {'color': 'pink', 'size': 'middle'},
        'name': 'Chebyx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers,
    ).json()
    object_id = response['id']
    yield object_id
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{object_id}'
    )


@pytest.fixture()
def create_for_del():
    body = {
        'data': {'color': 'pink', 'size': 'middle'},
        'name': 'Chebyx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers,
    ).json()
    obj_id = response['id']
    yield obj_id


@pytest.fixture(scope='session')
def run():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def one_test():
    print("before test")
    yield
    print("after test")


def test_all_object(run, one_test):
    response = requests.get(
        'http://objapi.course.qa-practice.com/object'
    )
    print(response.json())
    assert response.status_code == 200


@pytest.mark.parametrize('bodys', [
    {'data': {'color': 'pink', 'size': 'middle'}, 'name': 'Chebyx'},
    {'data': {'color': 'green', 'size': 'big'}, 'name': 'Rabbit'},
    {'data': {'color': 'grey', 'size': 'smole'}, 'name': 'Hot'}
])
def test_creation_object(bodys, one_test):
    body = bodys
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers,
    )
    assert response.status_code == 200


def test_one_object(create, one_test):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{create}'
    )
    assert response.status_code == 200
    assert response.json()['id'] == create


def test_change_object(create, one_test):
    body = {
        'data': {'color': 'green', 'size': 'middle'},
        'name': 'Onyx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{create}',
        json=body,
        headers=headers,
    )
    assert response.json()['name'] == 'Onyx'
    assert response.status_code == 200


@pytest.mark.critical
def test_change_object_patch(create, one_test):
    body = {
        'name': 'Onyxxxx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{create}',
        json=body,
        headers=headers,
    )
    assert response.json()['name'] == 'Onyxxxx'
    assert response.status_code == 200


@pytest.mark.medium
def test_delete(one_test):
    body = {
        'data': {'color': 'pink', 'size': 'middle'},
        'name': 'Chebyx'
    }

    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body
    )

    obj_id = response.json()['id']

    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{obj_id}'
    )

    assert response.status_code == 200
