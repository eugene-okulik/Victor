import requests
from endpoints.endpoint import Endpoint
import allure


class PatchObject(Endpoint):
    @allure.step('Patch objecct')
    def change_patch_object(self, post_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}', json=body, headers=headers,)
        self.json = self.response.json()
        return self.response
