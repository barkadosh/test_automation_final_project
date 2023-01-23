import time
import pytest
from utilities.common_ops import get_data, By
from workflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class TestWeb:
    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_grafana_title("Welcome to Grafana")

    # def test_verify_upper_menu(self):
    #     WebFlows.verify_menu_buttons_flow_smart_assertions()   # smart-assertions
    #     #WebFlows.verify_menu_buttons_flow()                   # my implementation

    def test_verify_new_users(self):
        WebFlows.open_users_page()
        WebFlows.create_user('test1', 'test1@test', 'test1user', '123456')
        WebFlows.open_users_page()
        WebFlows.create_user('test2', 'test2@test', 'test2user', '123456')
        WebFlows.open_users_page()
        WebFlows.verify_number_of_users(3)

    def test_verify_deleted_user(self):
        WebFlows.open_users_page()
        WebFlows.delete_user(By.USER, 'test1user')
        WebFlows.delete_user(By.INDEX, 2)
        WebFlows.verify_number_of_users(1)

    def teardown_method(self):
        WebFlows.grafana_home(self)





