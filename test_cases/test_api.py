# documentation : https://grafana.com/docs/grafana/latest/developers/http_api/team/#get-team-by-id
# curl http://admin:admin@localhost:3000/api/teams/search?name=test (view in cmd)
# To run: python -m pytest test_api.py -m run_this --alluredir=../allure-results

import json
import allure
import pytest

from extensions.verifications import Verifications
from requests.auth import HTTPBasicAuth
import requests
from workflows.api_flows import APIFlows

team_name = 'Test api'
team_email = 'testapi@gmail.com'
url = 'http://localhost:3000/'
resources = 'api/teams'
user = 'admin'
password = 'admin'
header = {'Content-Type': 'application/json'}


class Test_Api:
    @allure.title('TC01: Create team & verify status code')
    @allure.description('This test create new team in grafana')
    def test_create_and_verify_team(self):
        actual = APIFlows.crete_team(team_name, team_email)
        Verifications.verify_equals(actual, 200)

    @allure.title('TC02: Verify team name')
    @allure.description('This test verify grafana team name')
    def test_verify_team_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)

    @allure.title('TC03: Update team name')
    @allure.description('This test update grafana team name')
    def test_update_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.update_team(team_name + 'bar', team_email, id)
        Verifications.verify_equals(actual, 200)

    @allure.title('TC04: Verify updated team name')
    @allure.description('This test verify grafana team name')
    def test_verify_updated_team_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name + 'bar')

    @allure.title('TC04: Verify updated team name')
    @allure.description('This test verify grafana updated team name')
    def test_verify_updated_team_name(self):
        nodes = ['teams', 0, 'name']
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name + 'bar')

    @allure.title('TC05: Delete team')
    @allure.description('This test delete grafana team')
    def test_verify_updated_team_name(self):
        nodes = ['teams', 0, 'id']
        id = APIFlows.get_value_from_api(nodes)
        actual = APIFlows.delete_team(id)
        Verifications.verify_equals(actual, 200)


# ~~~ My test cases ~~~

