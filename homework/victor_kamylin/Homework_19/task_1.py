import requests


def all_object():
    response = requests.get(
        'http://objapi.course.qa-practice.com/object'
    )
    print(response.json())
    print(response.status_code)


def creation_object():
    body = {
        'data': {'color': 'pink', 'size': 'middle'},
        'name': 'Chebyx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers,
    )
    print(response.json())
    print(response.status_code)
    response = response.json()
    return response['id']


def one_object(id):
    response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{id}'
    )
    print(response.json())
    print(response.status_code)


def change_object(id):
    body = {
        'data': {'color': 'green', 'size': 'middle'},
        'name': 'Onyx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{id}',
        json=body,
        headers=headers,
    )
    print(response.json())
    print(response.status_code)


def change_object_patch(id):
    body = {
        'name': 'Onyxxxx'
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{id}',
        json=body,
        headers=headers,
    )
    print(response.json())
    print(response.status_code)


def delete(id):
    response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{id}'
    )
    print(response)


all_object()
new_id = creation_object()
one_object(new_id)
change_object(new_id)
change_object_patch(new_id)
delete(new_id)
