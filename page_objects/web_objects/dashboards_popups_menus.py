from selenium.webdriver.common.by import By

new_dashboard = (By.XPATH, "//li[@data-key='dashboards/new']")
browse_dashboards = (By.XPATH, "//li[@data-key='dashboards/browse']")
# Stared dashboards popup
stared_dashboard = (By.CSS_SELECTOR, "a>div>.css-6pogpz")


class DashboardPopup:
    def __init__(self, driver):
        self.driver = driver

    def get_new_dashboard(self):
        return self.driver.find_element(new_dashboard[0], new_dashboard[1])

    def get_browse_dashboards(self):
        return self.driver.find_element(browse_dashboards[0], browse_dashboards[1])

    def get_stared_dashboard(self):
        return self.driver.find_element(stared_dashboard[0], stared_dashboard[1])
