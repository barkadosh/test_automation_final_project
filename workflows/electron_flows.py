import time

import allure

import pytest
from selenium.webdriver.common.keys import Keys

from extensions.ui_actions import UiActions
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
    @allure.step("Click on completed tasks filter")
    def filter_tasks_completed():
        UiActions.click(page.electron_task.get_visibility_panel())
        time.sleep(3)  # Can't use a wait method, exception 'EventFiringWebElement' object is not subscriptable
        UiActions.click(page.electron_task.get_completed_filter())

    @staticmethod
    @allure.step("Click on completed tasks filter")
    def filter_all_tasks():
        UiActions.click(page.electron_task.get_all_filter())
        UiActions.click(page.electron_task. get_close_visibility_panel())

    @staticmethod
    @allure.step("Delete all tasks from the list")
    def delete_all_tasks_flow():
        for x in range(ElectronFlows.get_number_of_task_flow()):
            time.sleep(0.5)
            UiActions.mouse_hover_tooltip(page.electron_task.get_delete_buttons()[0])

    @staticmethod
    @allure.step("Add task with color")
    def add_colored_task_flow(task_name):
        UiActions.update_text(page.electron_task.get_create_field(), task_name)
        UiActions.click(page.electron_task.get_color_dropdown())
        UiActions.click(page.electron_task.get_color_green())
        UiActions.update_text(page.electron_task.get_create_field(), Keys.RETURN)

    @staticmethod
    @allure.step("Drag a new task to the bottom of the list")
    def change_task_position():
        UiActions.drag_element_by_coordinates(page.electron_task.get_drag_task()[0],1331,88.59)
