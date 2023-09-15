import allure
import pytest
from smart_assertions import soft_assert, verify_expectations

from selenium.webdriver.remote.webelement import WebElement


class Verifications:
    @staticmethod
    @allure.step("Verify list of actual elements is equal to expected elements")
    def verify_equals(actual, expected):
        assert actual == expected, f'Verify Equals Failed, Actual: {str(actual)} is not equal to Expected: {str(expected)}'

    @staticmethod
    @allure.step("Verify list of elements is equal to list of expected elements")
    def verify_lists_are_equals(actual, expected):
        for i in range(len(actual)):
            assert actual[i] == expected[i], f'Verify Equals Failed, Actual: {str(actual)} is not equal to Expected: {str(expected)}'
            i += 1


    @staticmethod
    @allure.step("Verify there's an element from a list of elements that equal to expected and return that element")
    def verify_equals_from_list(elems, expected):
        for i in range(0, len(elems)):
            actual = elems[i].text
            if actual == expected:
                return elems[i]
            else:
                i += 1

    @staticmethod
    @allure.step("Verify element is displayed")
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify Is Displayed Failed, Element: {elem.text} is not displayed'

    @staticmethod
    @allure.step("Verify element is not displayed")
    def is_not_displayed(elem: WebElement):
        assert not elem.is_displayed(), f'Verify Is Not Displayed Failed, Element: {elem.text} is displayed'

    # Verify Menu Buttons Flow Soft Using smart-assertions
    @staticmethod
    @allure.step("Soft verification of elements using smart-assertions")
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()

    # Verify Menu Buttons Flow Using My Implementation
    @staticmethod
    @allure.step("Soft verification of elements using my implementation")
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print(f'Soft Displayed Failed, Elements which have failed: {str(failed_elem)}')
            raise AssertionError('Soft Displayed Failed')

    @staticmethod
    @allure.step("Verify number of elements in list")
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, f'Number of elements in list: {str(len(elems))} does not match Expected: {str(size)}'





