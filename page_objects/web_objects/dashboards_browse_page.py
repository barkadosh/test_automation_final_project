from selenium.webdriver.common.by import By

collapse_folder = (By.CLASS_NAME, "css-1w3h79v")
dashboard_name = (By.CSS_SELECTOR, ".css-1cqw476")
search_bar = (By.CLASS_NAME, "css-1mlczho-input-input")
dashboard_checkbox = (By.XPATH, "//div[@class='css-yzyzzx']/label/span[@class='css-10xnr05']")
delete_button = (By.CLASS_NAME, "css-mk7eo3-button")
approve_delete_button = (By.XPATH, "//button[@aria-label='Confirm Modal Danger Button']")
# dashboard page
favorite_button = (By.XPATH, "//button[@aria-label='Mark as favorite']")
panel_title_bar = (By.CLASS_NAME, "panel-title")
save_dashboard = (By.XPATH, "//*[@aria-label='Save dashboard']")
modal_save_dashboard = (By.XPATH, "//*[@aria-label='Dashboard settings Save Dashboard Modal Save button']")


class BrowseDashboards:
    def __init__(self, driver):
        self.driver = driver

    def get_collapse_folder(self):
        return self.driver.find_element(collapse_folder[0], collapse_folder[1])

    def get_dashboards_names(self):
        return self.driver.find_elements(dashboard_name[0], dashboard_name[1])

    def get_favorite_button(self):
        return self.driver.find_element(favorite_button[0], favorite_button[1])

    def get_search_bar(self):
        return self.driver.find_element(search_bar[0], search_bar[1])

    def get_dashboard_checkbox(self):
        return self.driver.find_element(dashboard_checkbox[0], dashboard_checkbox[1])

    def get_delete_button(self):
        return self.driver.find_element(delete_button[0], delete_button[1])

    def get_approve_delete_button(self):
        return self.driver.find_element(approve_delete_button[0], approve_delete_button[1])

    def get_panel_title_bar(self):
        return self.driver.find_element(panel_title_bar[0], panel_title_bar[1])

    def get_save_dashboard(self):
        return self.driver.find_element(save_dashboard[0], save_dashboard[1])

    def get_modal_save_dashboard(self):
        return self.driver.find_element(modal_save_dashboard[0], modal_save_dashboard[1])