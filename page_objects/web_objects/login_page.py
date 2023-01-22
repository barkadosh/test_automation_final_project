from selenium.webdriver.common.by import By


class LoginPage:
    user_name = (By.NAME, "user")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")
    skip_button = (By.XPATH, "//span[text()='Skip']")

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(*LoginPage.user_name)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_skip(self):
        return self.driver.find_element(*LoginPage.skip_button)