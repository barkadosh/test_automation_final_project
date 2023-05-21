from selenium.webdriver.common.by import By

new_dashboard = (By.CSS_SELECTOR, "a[href='/dashboard/new']")
brows_dashboards = (By.CSS_SELECTOR, "a[href='/dashboards'].css-wdl7ag")

class DashboardPopup:
    def __init__(self, driver):
        self.driver = driver

    def get_new_dashboard(self):
        return self.driver.find_element(new_dashboard[0], new_dashboard[1])

    def get_brows_dashboards(self):
        return self.driver.find_element(brows_dashboards[0], brows_dashboards[1])

