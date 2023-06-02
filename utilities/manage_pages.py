import test_cases.conftest as conf
from page_objects.desktop_objects.standrad_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.dashboards_new_dashboard_page import NewDashboard
from page_objects.web_objects.dashboards_popups_menus import DashboardPopup
from page_objects.web_objects.dashboards_browse_page  import BrowseDashboards
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
web_dashboards_popups_menus = None
web_dashboards_new_dashboard_page = None
web_dashboards_browse_page = None

# Mobile Objects
mobile_calculator = None
mobile_save = None

# Electron Objects
electron_task = None

# Electron Objects
standard_calc = None


class ManagePages:

    ###########################################
    # Function Name: init_web_pages
    # Function Description: Initiate the pages of web page objects for the init_web_driver function
    ###########################################
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_main'] = MainPage(conf.driver)
        globals()['web_upper_menu'] = UpperMenuPage(conf.driver)
        globals()['web_side_menu_nav'] = SideMenuNav(conf.driver)
        # Server Admin
        globals()['web_server_admin_popup_menu'] = ServerAdminPopUp(conf.driver)
        globals()['web_server_admin'] = ServerAdminPage(conf.driver)
        globals()['web_server_admin_new_user'] = ServerAdminNewUser(conf.driver)
        # Dashboards
        globals()['web_dashboards_popups_menus'] = DashboardPopup(conf.driver)
        globals()['web_dashboards_new_dashboard_page'] = NewDashboard(conf.driver)
        globals()['web_dashboards_browse_page'] = BrowseDashboards(conf.driver)

    ###########################################
    # Function Name: init_mobile_pages
    # Function Description: Initiate the pages of mobile page objects for the init_mobile_driver function
    ###########################################
    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_save'] = SavedPage(conf.driver)

    ###########################################
    # Function Name: init_electron_pages
    # Function Description: Initiate the pages of electron page objects for the init_electron_driver function
    ###########################################
    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)

    ###########################################
    # Function Name: init_desktop_pages
    # Function Description: Initiate the pages of desktop page objects for the init_desktop_driver function
    ###########################################
    @staticmethod
    def init_desktop_pages():
        globals()['standard_calc'] = StandardPage(conf.driver)
