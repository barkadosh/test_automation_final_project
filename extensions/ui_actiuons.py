import allure

from selenium.webdriver.remote.webelement import WebElement

import test_cases.conftest as conf


class UiActions:
    @staticmethod
    @allure.step("Click on element")
    def click(elem: WebElement):
        # explicitly wait...
        elem.click()

    @staticmethod
    @allure.step("Updating text")
    def update_text(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step("Mouse hover to elements")
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step("Right click")
    def right_click(elem: WebElement):
        conf.action.context_click(elem).perform()

    @staticmethod
    @allure.step("Drag and drop")
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step("Clear text field in elements")
    def clear(elem: WebElement):
        elem.clear()

