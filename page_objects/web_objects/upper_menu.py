from selenium.webdriver.common.by import By

general_breadcrumbs = (By.LINK_TEXT, "General")
home_breadcrumbs = (By.LINK_TEXT, "Home")
panel = (By.CSS_SELECTOR, "[aria-label='Add panel']")
dashboard_settings = (By.CSS_SELECTOR, "[aria-label='Dashboard settings']")
cycle_view = (By.CSS_SELECTOR, "[aria-label='Cycle view mode']")


class UpperMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_general_breadcrumbs(self):
        return self.driver.find_element(general_breadcrumbs[0], general_breadcrumbs[1])

    def get_home_breadcrumbs(self):
        return self.driver.find_element(home_breadcrumbs[0], home_breadcrumbs[1])

    def get_panel(self):
        return self.driver.find_element(panel[0], panel[1])

    def get_dashboard_settings(self):
        return self.driver.find_element(dashboard_settings[0], dashboard_settings[1])

    def get_cycle_view(self):
        return self.driver.find_element(cycle_view[0], cycle_view[1])
