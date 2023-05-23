import allure

from selenium.webdriver import ActionChains
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

    # For electron app - need to define here the action chains because the app rendering all the time-
    @staticmethod
    @allure.step("Mouse hover tooltip")
    def mouse_hover_tooltip(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).click().perform()

    @staticmethod
    @allure.step("Mouse hover on a element without clicking")
    def mouse_hover_element(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).perform()

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
    @allure.step("Drag an element")
    def drag_element(elem: WebElement):
        conf.action.click_and_hold(elem).move_by_offset(50,0).release().perform()

    # This function gets x, y coordinates and scroll to that location
    @staticmethod
    @allure.step("Scroll to element location")
    def scroll_to_element(x, y):
        conf.driver.execute_script(f"scrollTo({x},{y})")


    @staticmethod
    @allure.step("Clear text field in elements")
    def clear(elem: WebElement):
        elem.clear()

