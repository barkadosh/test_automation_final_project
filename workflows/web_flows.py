import allure
import pytest

import page_objects.web_objects.main_page as main
import page_objects.web_objects.server_admin_page
import page_objects.web_objects.dashboards_popups_menus
import page_objects.web_objects.dashboards_new_dashboard_page
from extensions.ui_actiuons import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, wait_for_element_text, get_data, read_csv
from utilities.enums import For


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
        # I added this step because the alert interrupt clicking on the users_list element
        UiActions.click(page.web_server_admin.close_alert())

    # Flows related to creating and managing dashboards
    @staticmethod
    @allure.step("Go to home page flow")
    def grafana_home(self):
        self.driver.get(get_data('Url'))

    @staticmethod
    @allure.step("Open create dashboard page")
    def open_create_dashboard_page():
        elem1 = page.web_side_menu_nav.get_dashboards_nav()
        UiActions.mouse_hover_element(elem1)
        # wait(For.ELEMENT_EXIST, page_objects.web_objects.dashboards_popup_menu.new_dashboard)
        elem2 = page.web_dashboards_popups_menus.get_new_dashboard()
        UiActions.mouse_hover_tooltip(elem2)

    @staticmethod
    @allure.step("Add settings and create new panel dashboard")
    def create_dashboard():
        UiActions.click(page.web_dashboards_new_dashboard_page.get_new_panel())
        UiActions.clear(page.web_dashboards_new_dashboard_page.get_add_dashboard_title())
        UiActions.update_text(page.web_dashboards_new_dashboard_page.get_add_dashboard_title(), 'Test')
        UiActions.update_text(page.web_dashboards_new_dashboard_page.get_add_dashboard_description(),
                              'This is a test dashboard')
        UiActions.click(page.web_dashboards_new_dashboard_page.get_add_link())
        UiActions.update_text(page.web_dashboards_new_dashboard_page.get_link_title(), 'Test Link')
        UiActions.update_text(page.web_dashboards_new_dashboard_page.get_link_url(),
                              'https://noc.co.il/')
        UiActions.click(page.web_dashboards_new_dashboard_page.get_save_url())
        UiActions.click(page.web_dashboards_new_dashboard_page.get_table_mode())
        UiActions.click(page.web_dashboards_new_dashboard_page.get_placement_right())
        UiActions.click(page.web_dashboards_new_dashboard_page.get_time_zone())
        UiActions.click(page.web_dashboards_new_dashboard_page.get_browser_time())
        UiActions.scroll_to_element(page.web_dashboards_new_dashboard_page.get_line_width_slider())
        UiActions.drag_element(page.web_dashboards_new_dashboard_page.get_line_width_slider())
        UiActions.drag_element(page.web_dashboards_new_dashboard_page.get_fill_opacity_slider())
        UiActions.click(page.web_dashboards_new_dashboard_page.get_apply_dashboard())
        UiActions.click(page.web_dashboards_new_dashboard_page.get_save_dashboard())
        UiActions.clear(page.web_dashboards_new_dashboard_page.get_add_dashboard_name())
        UiActions.update_text(page.web_dashboards_new_dashboard_page.get_add_dashboard_name(),
                              get_data("dashboard_name"))
        UiActions.click(page.web_dashboards_new_dashboard_page.get_save_new_dashboard())

    @staticmethod
    @allure.step("Verify the new dashboard was created by name and title")
    def verify_new_dashboard():
        wait_for_element_text(For.ELEMENT_TEXT_PRESENT, page_objects.web_objects.dashboards_new_dashboard_page
                              .dashboard_name, get_data("dashboard_name"))
        actual_name = page.web_dashboards_new_dashboard_page.get_dashboard_name().text
        Verifications.verify_equals(actual_name, get_data("dashboard_name"))
        actual_title = page.web_dashboards_new_dashboard_page.get_dashboard_title().text
        Verifications.verify_equals(actual_title, 'Test')

    @staticmethod
    @allure.step("Open Browse page")
    def open_brows_dashboards_page():
        UiActions.click(page.web_side_menu_nav.get_dashboards_nav())

    # This function search in the dashboard list the expected dashboard and open it,
    # if the dashboard not exist it report it to the log
    @staticmethod
    @allure.step("Open Dashboard's board")
    def open_a_dashboard_board():
        UiActions.click(page.web_dashboards_browse_page.get_collapse_folder())
        elems = page.web_dashboards_browse_page.get_dashboards_names()
        expected = get_data("dashboard_name")
        try:
            elem_dashboard = Verifications.verify_equals_from_list(elems, expected)
            UiActions.click(elem_dashboard)
        except Exception as e:
            print(f"This dashboard doesn't exist, error: {e}")
            pytest.fail()

    @staticmethod
    @allure.step("Mark dashboard as favorite and verify it appear's in the stared popup menu")
    def favorite_a_dashboard_and_verify():
        UiActions.click(page.web_dashboards_browse_page.get_favorite_button())
        UiActions.click_and_hold(page.web_side_menu_nav.get_starred_nav())
        actual = page.web_dashboards_popups_menus.get_stared_dashboard().text
        expected = get_data("dashboard_name")
        Verifications.verify_equals(actual, expected)


# Parameters for "TC04: Filter the users list" from test_web.py, imported from Users_CSV File
data = read_csv(get_data('Users_CSV'))
users_testdata = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]
