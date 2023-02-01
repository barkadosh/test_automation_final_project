from selenium.webdriver.common.by import By

user_name = (By.NAME, "user")


class SavedPage:
    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(user_name[0], user_name[1])
