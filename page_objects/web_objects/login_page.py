from selenium.webdriver.common.by import By

user_name = (By.NAME, "user")
password = (By.NAME, "password")
login_button = (By.XPATH, "//button[@type='submit']")
skip_button = (By.XPATH, "//span[text()='Skip']")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(user_name[0], user_name[1])

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_submit(self):
        return self.driver.find_element(login_button[0], login_button[1])

    def get_skip(self):
        return self.driver.find_element(skip_button[0], skip_button[1])
