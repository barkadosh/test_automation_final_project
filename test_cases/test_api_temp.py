# documentation : https://grafana.com/docs/grafana/latest/developers/http_api/team/#get-team-by-id
# curl http://admin:admin@localhost:3000/api/teams/search?name=test
import json

from requests.auth import HTTPBasicAuth

import requests

url = 'http://localhost:3000/'
resources = 'api/teams'
user = 'admin'
password = 'admin'
header = {'Content-Type': 'application/json'}


class Test_Api_Temp:
    def test_01_create_team(self):
        payload = {
            "name": "MyTestTeam",
            "email": "email@test.com",
            "orgId": 2
        }
        response = requests.post(url + resources, json=payload, headers=header,  auth=HTTPBasicAuth(user, password))
        response_json = response.json()
        print(json.dumps(response_json, indent=2))
        assert response.status_code == 200

    def test_02_get_team(self):
        response = requests.get(url + resources + '/search', auth=HTTPBasicAuth(user, password))
        response_json = response.json()
        #print(json.dumps(response_json, indent=2))
        my_team_id = response_json['teams'][0]['id']
        print(my_team_id)
