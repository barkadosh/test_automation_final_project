import test_cases.conftest as conf
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage


# Web Objects
web_login = None
web_main = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
