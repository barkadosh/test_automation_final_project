from selenium.webdriver.common.by import By

home_nav = (By.CSS_SELECTOR, "[aria-label='Home']")
open_navigation_menu = (By.CSS_SELECTOR, "[aria-label='Open navigation menu']")
search_nav = (By.CSS_SELECTOR, "[aria-label='Search dashboards']")
starred_nav = (By.CSS_SELECTOR, "[aria-label='Starred']")
dashboards_nav = (By.CSS_SELECTOR, "[aria-label='Dashboards']")
explore_nav = (By.CSS_SELECTOR, "[aria-label='Explore']")
alerting_nav = (By.CSS_SELECTOR, "[aria-label='Alerting']")
configuration_nav = (By.CSS_SELECTOR, "[aria-label='Configuration']")
server_admin_nav = (By.CSS_SELECTOR, "[aria-label='Server admin']")
admin_nav = (By.CSS_SELECTOR, "[aria-label='admin']")
help_nav = (By.CSS_SELECTOR, "[aria-label='Help']")

class SideMenuNav:
    def __init__(self, driver):
        self.driver = driver

    def get_home_nav(self):
        return self.driver.find_element(home_nav[0], home_nav[1])

    def get_open_navigation_menu(self):
        return self.driver.find_element(open_navigation_menu[0], open_navigation_menu[1])

    def get_search_nav(self):
        return self.driver.find_element(search_nav[0], search_nav[1])

    def get_starred_nav(self):
        return self.driver.find_element(starred_nav[0], starred_nav[1])

    def get_dashboards_nav(self):
        return self.driver.find_element(dashboards_nav[0], dashboards_nav[1])

    def get_explore_nav(self):
        return self.driver.find_element(explore_nav[0], explore_nav[1])

    def get_alerting_nav(self):
        return self.driver.find_element(alerting_nav[0], alerting_nav[1])

    def get_configuration_nav(self):
        return self.driver.find_element(configuration_nav[0], configuration_nav[1])

    def get_server_admin_nav(self):
        return self.driver.find_element(server_admin_nav[0], server_admin_nav[1])

    def get_admin_nav(self):
        return self.driver.find_element(admin_nav[0], admin_nav[1])

    def get_help_nav(self):
        return self.driver.find_element(help_nav[0], help_nav[1])
