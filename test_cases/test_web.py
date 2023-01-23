import time
import pytest
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_grafana_title("Welcome to Grafana")

    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flow_smart_assertions()   # smart-assertions
        #WebFlows.verify_menu_buttons_flow()                   # my implementation

    def verify_new_users(self):
        WebFlows.open_users_page()
        WebFlows.create_user('test1', 'test1@test', 'test1user', '123456')




