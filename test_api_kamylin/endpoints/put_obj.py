import requests
from endpoints.endpoint import Endpoint
import allure


class PutObj(Endpoint):
    @allure.step('Put object')
    def change_object(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}', json=body, headers=headers,)
        self.json = self.response.json()
        return self.response
