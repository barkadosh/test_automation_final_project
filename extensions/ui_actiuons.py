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
    @allure.step("Click and hold")
    def click_and_hold(elem: WebElement):
        ActionChains(conf.driver).click_and_hold(elem).perform()

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

    # Click anywhere on element and drag it to specified location by coordinates
    @staticmethod
    @allure.step("Drag an element with coordinates")
    def drag_element_by_coordinates(elem: WebElement, x, y):
        conf.action.click_and_hold(elem).move_by_offset(x, y).release().perform()

    @staticmethod
    @allure.step("Move to element with coordinates, click and hold and drag")
    def move_to_element_by_coordinates(elem: WebElement, x, y):
        width = elem.rect['x']
        height = elem.rect['y']
        conf.action.move_to_element_with_offset(elem, width, height). \
            click_and_hold().move_by_offset(x, y).release().perform()

    # This function gets x, y coordinates and scroll to that location
    @staticmethod
    @allure.step("Scroll to element location")
    def scroll_to_element(elem):
        conf.driver.execute_script("arguments[0].scrollIntoView();", elem)

    @staticmethod
    @allure.step("Clear text field in elements")
    def clear(elem: WebElement):
        elem.clear()
