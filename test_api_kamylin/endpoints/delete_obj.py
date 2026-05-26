import requests
from endpoints.endpoint import Endpoint
import allure


class DeleteObj(Endpoint):
    @allure.step('Delete object')
    def delete_obj(self, obj_id):
        self.response = requests.delete(f'{self.url}/{obj_id}')
        return self.response
