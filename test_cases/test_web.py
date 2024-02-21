import allure

import time
import pytest
from test_cases import conftest as conf
from test_cases.conftest import eyes
from utilities.common_ops import get_data, save_screenshot
from utilities.enums import By
from workflows import web_flows
from workflows.web_flows import WebFlows


# Run command: python -m pytest test_web.py::TestWebUsers  -s -v -m run_this --alluredir=../allure-results

@pytest.mark.usefixtures('init_web_driver')
class TestWebUsers:
    @allure.title("TC01: Login to Grafana")
    @allure.description("Verify a successful login to Grafana")
    @pytest.mark.sanity
    @pytest.mark.visual_test
    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_grafana_title("Welcome to Grafana")

    @allure.title("TC02: Check upper menu buttons")
    @allure.description("This test check that the upper menu buttons are displayed")
    @pytest.mark.sanity
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flow_smart_assertions()  # smart-assertions

    #     #WebFlows.verify_menu_buttons_flow()                   # my implementation

    @allure.title("TC03: Create and verify new users")
    @allure.description("This test create new users and check that the new users are displayed")
    def test_verify_new_users(self):
        WebFlows.open_users_page()
        time.sleep(5)
        WebFlows.create_user('test1', 'test1@gmail.com', 'test1user', '123456')
        WebFlows.open_users_page()
        WebFlows.create_user('test2', 'test2@gmail.com', 'test2user', '123456')
        WebFlows.open_users_page()
        WebFlows.verify_number_of_users(3)

    @allure.title("TC04: Filter the users list")
    @allure.description("This test filters the users list and check that the correct number of users are displayed")
    @pytest.mark.parametrize('search_value, expected_users', web_flows.users_testdata)
    def test_search_filter(self, search_value, expected_users):
        WebFlows.open_users_page()
        WebFlows.search_user(search_value)
        WebFlows.verify_number_of_users(int(expected_users))

    @allure.title("TC05: Delete users")
    @allure.description("This test delete new users and check that the users are deleted")
    def test_verify_deleted_user(self):
        WebFlows.open_users_page()
        WebFlows.delete_user(By.USER, 'test1user')
        WebFlows.delete_user(By.INDEX, 1)
        WebFlows.verify_number_of_users(1)

    @allure.title("TC06: Visual testing - users chart")
    @allure.description("Check visually the users chart")
    @pytest.mark.visual_test
    @pytest.mark.skipif(get_data("ExecuteApplitools").lower() == 'no', reason='Want to view Event Listeners')
    def test_view_users_chart(self):
        WebFlows.open_users_page()
        eyes.open(conf.driver, "Grafana - users chart", "Check visually the users chart")
        eyes.check_window("Check users table")

    def teardown_method(self):
        WebFlows.grafana_home(self)
        time.sleep(2)


# Run command: python -m pytest test_web.py::TestWebDashboard -s -v -m run_this --alluredir=../allure-results
@pytest.mark.usefixtures('init_web_driver')
class TestWebDashboard:
    @allure.title("TC01: Setup and create new dashboard ")
    @allure.description("Add settings, create and verify new dashboard in grafana")
    def test_create_new_dashboard(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.open_create_dashboard_page()
        WebFlows.create_dashboard_changed_settings()
        WebFlows.verify_new_dashboard()

    @allure.title("TC02: Favorite a dashboard")
    @allure.description("Add dashboard to Favorite and validate the dashboard appear in the favorite menu")
    def test_favorite_a_dashboard(self):
        WebFlows.open_brows_dashboards_page()
        WebFlows.open_a_dashboard_board()
        WebFlows.favorite_a_dashboard_and_verify()
        save_screenshot()

    @allure.title("TC03: Change position of a dashboard")
    @allure.description("Drag a dashboard to another position and change is size")
    def test_change_position_and_size(self):
        WebFlows.open_starred_dashboard()
        WebFlows.change_dashboard_position()

    @allure.title("TC04: Delete a dashboard")
    @allure.description("Delete a dashboard from the browse dashboards page")
    @pytest.mark.run_this
    def test_delete_a_dashboard(self):
        WebFlows.open_brows_dashboards_page()
        WebFlows.search_and_check_dashboard()
        WebFlows.delete_dashboard()
        save_screenshot()

    def teardown_method(self):
        time.sleep(3)
        WebFlows.grafana_home(self)
        time.sleep(1)

