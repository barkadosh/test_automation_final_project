import allure

import pytest
from workflows.db_flows import DBFlows
from workflows.web_flows import WebFlows

# Run command: python -m pytest test_web_db.py -s -v --alluredir=../allure-results
# Notice: need to be run only with command line when starting grafana server with subprocess
@pytest.mark.usefixtures('init_web_driver', 'init_db_connector')
class TestWebDB:
    @allure.title('Test01: Login to grafana via DB')
    @allure.description('This test verify login using elements taking from DB')
    def test_verify_login_db(self):
        DBFlows.login_grafana_via_db()
        WebFlows.verify_grafana_title("Welcome to Grafana")
