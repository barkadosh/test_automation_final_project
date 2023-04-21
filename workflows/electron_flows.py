import time

import allure
from selenium.webdriver.common.keys import Keys

from extensions.ui_actiuons import UiActions
import utilities.manage_pages as page


class ElectronFlows:
    @staticmethod
    @allure.step("Add new task flow")
    def add_new_task_flow(task_name):
        UiActions.update_text(page.electron_task.get_create_field(), task_name)
        UiActions.update_text(page.electron_task.get_create_field(), Keys.RETURN)

    @staticmethod
    @allure.step("Get the number of tasks flow")
    def get_number_of_task_flow():
        return len(page.electron_task.get_tasks())

    @staticmethod
    @allure.step("Delete all tasks from the list")
    def delete_all_tasks():
        for x in range(ElectronFlows.get_number_of_task_flow()):
            time.sleep(0.5)
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])


