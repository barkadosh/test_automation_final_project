import time

import allure

import page_objects.web_objects.main_page as main
import page_objects.web_objects.server_admin_page
from extensions.ui_actiuons import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For, get_data, read_csv


class WebFlows:

    @staticmethod
    @allure.step("Login to Grafana flow")
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())

    @staticmethod
    @allure.step("Verify Grafana title flow")
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXIST, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    # Verify Menu Buttons Flow Soft Using smart-assertions
    @staticmethod
    @allure.step("Verify displayed upper menu buttons using smart assertions flow")
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_general_breadcrumbs(),
                 page.web_upper_menu.get_home_breadcrumbs(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_assert(elems)

    # Verify Menu Buttons Flow Soft Using My Implementation
    @staticmethod
    @allure.step("Verify displayed upper menu buttons using my implementation flow")
    def verify_menu_buttons_flow():
        elems = [page.web_upper_menu.get_general_breadcrumbs(),
                 page.web_upper_menu.get_home_breadcrumbs(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_displayed(elems)

    @staticmethod
    @allure.step("Go to users page flow")
    def open_users_page():
        elem1 = page.web_side_menu_nav.get_server_admin_nav()
        elem2 = page.web_server_admin_popup_menu.get_users_nav()
        UiActions.mouse_hover(elem1, elem2)

    @staticmethod
    @allure.step("Create new users flow")
    def create_user(name, email, user, password):
        UiActions.click(page.web_server_admin.get_new_user())
        UiActions.update_text(page.web_server_admin_new_user.get_name(), name)
        UiActions.update_text(page.web_server_admin_new_user.get_email(), email)
        UiActions.update_text(page.web_server_admin_new_user.get_username(), user)
        UiActions.update_text(page.web_server_admin_new_user.get_password(), password)
        UiActions.click(page.web_server_admin_new_user.get_create_user())

    @staticmethod
    @allure.step("Verify numbers of users in users table flow")
    def verify_number_of_users(number):
        if number > 0:
            wait(For.ELEMENT_DISPLAYED, page_objects.web_objects.server_admin_page.users_list)
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(), number)
        elif number == 0:
            Verifications.verify_number_of_elements(page.web_server_admin.get_users_list(), number)
        else:
            raise Exception("Non legal number, please provide number higher or equal to 0")

    @staticmethod
    @allure.step("Search users in users table flow")
    def search_user(search_value):
        UiActions.clear(page.web_server_admin.get_search())
        UiActions.update_text(page.web_server_admin.get_search(), search_value)

    @staticmethod
    @allure.step("Delete users from users table flow")
    def delete_user(by, value):
        if by == 'user':
            UiActions.click(page.web_server_admin.get_user_by_username(value))
        if by == 'index':
            UiActions.click(page.web_server_admin.get_user_by_index(value))
        UiActions.click(page.web_server_admin.get_delete())
        UiActions.click(page.web_server_admin.confirm_delete())

    @staticmethod
    @allure.step("Go to home page flow")
    def grafana_home(self):
        self.driver.get(get_data('Url'))


data = read_csv(get_data('CSV_Location'))
testdata = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]
