import test_cases.conftest as conf
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.upper_menu_page import UpperMenuPage

# Web Objects
web_login = None
web_main = None
web_upper_menu = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
