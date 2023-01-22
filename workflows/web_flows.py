from extensions.ui_actiuons import UiActions
import utilities.manage_pages as page
from extensions.verifications import Verifications


class WebFlows:
    @staticmethod
    def login_flow(user: str, password: str):
        UiActions.update_text(page.web_login.get_user_name(), user)
        UiActions.update_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_submit())
        UiActions.click(page.web_login.get_skip())

    @staticmethod
    def verify_grafana_title(expected: str):
        # Expected issue
        actual = page.web_main.get_main_title().text
        Verifications.verify_equals(actual, expected)

