import requests
from endpoints.endpoint import Endpoint
import allure


class GetObject(Endpoint):
    @allure.step('Get all object')
    def test_all_object(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step('Get one object')
    def test_one_object(self, obj_id):
        self.response = requests.get(f'{self.url}/{obj_id}')
        self.json = self.response.json()
        return self.response
