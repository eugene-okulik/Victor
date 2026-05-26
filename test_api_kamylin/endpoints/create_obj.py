import requests
from endpoints.endpoint import Endpoint
import allure


class CreateObj(Endpoint):
    object_id = None

    @allure.step('Create new object')
    def create(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
