import allure

from extensions.db_actions import DBActions
from workflows.web_flows import WebFlows


class DBFlows:
    @staticmethod
    @allure.step('Login to grafana via data base flow')
    def login_grafana_via_db():
        columns = ['name', 'password']
        result = DBActions.get_query_result(columns, 'usersfinalprojectaut', 'comments', 'correct')
        WebFlows.login_flow(result[0][0], result[0][1])