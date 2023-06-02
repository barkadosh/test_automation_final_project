from selenium.webdriver.common.by import By

collapse_folder = (By.CLASS_NAME, "css-1w3h79v")
dashboard_name = (By.CSS_SELECTOR, ".css-1cqw476")
favorite_button = (By.XPATH, "//button[@aria-label='Mark as favorite']")


class BrowseDashboards:
    def __init__(self, driver):
        self.driver = driver

    def get_collapse_folder(self):
        return self.driver.find_element(collapse_folder[0], collapse_folder[1])

    def get_dashboards_names(self):
        return self.driver.find_elements(dashboard_name[0], dashboard_name[1])

    def get_favorite_button(self):
        return self.driver.find_element(favorite_button[0], favorite_button[1])