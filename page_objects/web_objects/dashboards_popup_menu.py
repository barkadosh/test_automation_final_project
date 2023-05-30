from selenium.webdriver.common.by import By

new_dashboard = (By.XPATH, "//li[@data-key='dashboards/new']")
browse_dashboards = (By.XPATH, "//li[@data-key='dashboards/browse']")


class DashboardPopup:
    def __init__(self, driver):
        self.driver = driver

    def get_new_dashboard(self):
        return self.driver.find_element(new_dashboard[0], new_dashboard[1])

    def get_browse_dashboards(self):
        return self.driver.find_element(browse_dashboards[0], browse_dashboards[1])
