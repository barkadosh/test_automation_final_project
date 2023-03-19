import test_cases.conftest as conf
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.main_page import MainPage
from page_objects.web_objects.server_admin_new_user_page import ServerAdminNewUser
from page_objects.web_objects.server_admin_page import ServerAdminPage
from page_objects.web_objects.server_admin_popup_menu import ServerAdminPopUp
from page_objects.web_objects.upper_menu import UpperMenuPage
from page_objects.web_objects.side_menu_nav import SideMenuNav

# Web Objects
web_login = None
web_main = None
web_upper_menu = None
web_side_menu_nav = None
web_server_admin_popup_menu = None
web_server_admin = None
web_server_admin_new_user = None

# Mobile Objects
mobile_calculator = None
mobile_save = None

# Electron Objects
electron_task = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
        globals()['web_side_menu_nav'] = SideMenuNav(conf.driver)
        globals()['web_server_admin_popup_menu'] = ServerAdminPopUp(conf.driver)
        globals()['web_server_admin'] = ServerAdminPage(conf.driver)
        globals()['web_server_admin_new_user'] = ServerAdminNewUser(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_save'] = SavedPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)
