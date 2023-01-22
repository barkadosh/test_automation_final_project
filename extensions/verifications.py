from selenium.webdriver.remote.webelement import WebElement


class Verifications:
    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f'Verify Equals Failed, Actual: {str(actual)} is notequal to Expected: {str(expected)}'

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify Is Displayed Failed, Element: {elem.text} is not displayed'

