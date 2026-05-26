from locust import task, HttpUser
import random


class ApiTest(HttpUser):

    def on_start(self):
        self.id = []

    @task(1)
    def get_all_obj(self):
        self.client.get(
            '/object', headers={'Content-Type': 'application/json'})

    @task(2)
    def creation_object(self):
        response = self.client.post(
            '/object',
            json={'data': {'color': 'pink', 'size': 'smole'}, 'name': 'Hot'},
            headers={'Content-Type': 'application/json'}
        )
        obj_id = response.json()['id']
        self.id.append(obj_id)

    @task(1)
    def one_object(self):
        if self.id:
            self.client.post(
                f'/object/{random.choice(self.id)}',
                headers={'Content-Type': 'application/json'}
            )

    @task(1)
    def one_delete(self):
        if self.id:
            self.client.delete(
                f'/object/{random.choice(self.id)}',
                headers={'Content-Type': 'application/json'}
            )
