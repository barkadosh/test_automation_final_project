from selenium.webdriver.common.by import By

main_title = (By.CLASS_NAME, "css-17tm80")



class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        return self.driver.find_element(main_title[0], main_title[1])
