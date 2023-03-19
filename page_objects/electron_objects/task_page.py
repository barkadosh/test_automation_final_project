from selenium.webdriver.common.by import By

create = (By.CSS_SELECTOR, "input.input_b5pqF")
tasks = (By.CSS_SELECTOR, "div.view_2Ow90")
delete_buttons = (By.CSS_SELECTOR, "div.view_2Ow90>svg")

class TaskPage:

    def __init__(self, driver):
        self.driver = driver

    def get_create(self):
        return self.driver.find_element(create[0], create[1])

    def get_tasks(self):
        return self.driver.find_elements(tasks[0], tasks[1])

    def get_delete_buttons(self):
        return self.driver.find_elements(delete_buttons[0], delete_buttons[1])