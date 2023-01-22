from selenium.webdriver.common.by import By


class MainPage:
    title = (By.CLASS_NAME, "css-17tm80")

    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        return self.driver.find_element(*MainPage.title)

