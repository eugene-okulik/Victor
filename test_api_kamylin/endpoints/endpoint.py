import allure


class Endpoint:
    response = None
    url = 'http://objapi.course.qa-practice.com/object'
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that status code = 200')
    def check_status_code(self):
        assert self.response.status_code == 200, f"Ожидался код 200, получен {self.response.status_code}"

    @allure.step('Check that id =created ID ')
    def check_response_id(self, create_id):
        assert self.response.json()['id'] == create_id

    @allure.step('Check that data is updated')
    def check_update_data(self, name):
        assert self.response.json()['name'] == name
