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

    @pytest.mark.run_this
    @allure.title('TC02: Verify team name')
    @allure.description('This test verify grafana team name')
    def test_verify_team_member_name(self):
        nodes = ('teams', 0, 'name')
        actual = APIFlows.get_value_from_api(nodes)
        Verifications.verify_equals(actual, team_name)




    def test_get_team_id(self):
        response = requests.get(url + resources + '/search', auth=HTTPBasicAuth(user, password))
        response_json = response.json()
        #print(json.dumps(response_json, indent=2))
        my_team = response_json['teams'][0]['name']
        print(my_team)
        # my_team_id = response_json['teams'][0]['id']
        # print(my_team_id)
