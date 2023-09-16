import time

import allure

import pytest
from selenium.webdriver.common.keys import Keys

from extensions.ui_actiuons import UiActions
import utilities.manage_pages as page
from utilities.common_ops import wait


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
    @allure.step("Click on the first task complete checkbox")
    def click_task_checkbox(i):
        UiActions.click(page.electron_task.get_complete_checkbox()[i])

    @staticmethod
    @allure.step("Click on the first task complete checkbox")
    def click_toggle_all_completed_checkbox():
        UiActions.click(page.electron_task.get_toggle_all_completed())

    @staticmethod
    @allure.step("Filter the list to show only completed tasks")
    def filter_to_tasks_completed():
        UiActions.click(page.electron_task.get_visibility_panel())
        wait("element_to_be_clickable", page.electron_task.get_completed_filter())
        UiActions.click(page.electron_task.get_completed_filter())

    @staticmethod
    @allure.step("Delete all tasks from the list")
    def delete_all_tasks_flow():
        for x in range(ElectronFlows.get_number_of_task_flow()):
            time.sleep(0.5)
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])
