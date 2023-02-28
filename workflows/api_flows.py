import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data('Url')
resources = 'api/teams/'
user = get_data('Username')
password = get_data('Password')


class APIFlows:
    @staticmethod
    @allure.step('Get value from Grafana api flow')
    def get_value_from_api(nodes):
        response = APIActions.get(url + resources + 'search', user, password)
        return APIActions.extract_value_from_response(response, nodes)

    @staticmethod
    @allure.step('Create new team in Grafana')
    def crete_team(name, email):
        payload = {'name': name, 'email': email}
        status_code = APIActions.post(url + resources, payload, user, password)
        return status_code

    @staticmethod
    @allure.step('update team in Grafana')
    def update_team(name, email, id):
        payload = {'name': name, 'email': email}
        status_code = APIActions.post(url + resources + str(id), payload, user, password)
        return status_code

    @staticmethod
    @allure.step('Delete team in Grafana')
    def delete_team(id):
        status_code = APIActions.delete(url + resources + str(id), user, password)
        return status_code
