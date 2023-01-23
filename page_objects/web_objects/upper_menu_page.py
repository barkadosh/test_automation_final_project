from selenium.webdriver.common.by import By

general = (By.LINK_TEXT, "General")
home = (By.LINK_TEXT, "Home")
panel = (By.CSS_SELECTOR, "[aria-label='Add panel']")
dashboard_settings = (By.CSS_SELECTOR, "[aria-label='Dashboard settings']")
cycle_view = (By.CSS_SELECTOR, "[aria-label='Cycle view mode']")


class UpperMenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_general(self):
        return self.driver.find_element(general[0], general[1])

    def get_home(self):
        return self.driver.find_element(home[0], home[1])

    def get_panel(self):
        return self.driver.find_element(panel[0], panel[1])

    def get_dashboard_settings(self):
        return self.driver.find_element(dashboard_settings[0], dashboard_settings[1])

    def get_cycle_view(self):
        return self.driver.find_element(cycle_view[0], cycle_view[1])
