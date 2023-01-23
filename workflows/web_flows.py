import page_objects.web_objects.main_page as main
from extensions.ui_actiuons import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from utilities.common_ops import wait, For


class WebFlows:
    @staticmethod
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())

    @staticmethod
    def verify_grafana_title(expected: str):
        wait(For.ELEMENT_EXIST, main.main_title)
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

    # Verify Menu Buttons Flow Soft Using smart-assertions
    @staticmethod
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_upper_menu.get_general(),
                 page.web_upper_menu.get_home(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_assert(elems)

    # Verify Menu Buttons Flow Soft Using smart-assertions
    @staticmethod
    def verify_menu_buttons_flow():
        elems = [page.web_upper_menu.get_general(),
                 page.web_upper_menu.get_home(),
                 page.web_upper_menu.get_panel(),
                 page.web_upper_menu.get_dashboard_settings(),
                 page.web_upper_menu.get_cycle_view()]
        Verifications.soft_displayed(elems)

