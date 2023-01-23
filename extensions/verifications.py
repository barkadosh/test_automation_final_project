from selenium.webdriver.remote.webelement import WebElement


class Verifications:
    @staticmethod
    def verify_equals(actual, expected):
        assert actual == expected, f'Verify Equals Failed, Actual: {str(actual)} is notequal to Expected: {str(expected)}'

    @staticmethod
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), f'Verify Is Displayed Failed, Element: {elem.text} is not displayed'

    @staticmethod
    def soft_displayed(elems):
        failed_elems = []
        for i in range(len(elems)):
            if not elems[i].is_displayed():
                failed_elems.insert(len(failed_elems), elems[i].get_attribute('aria-label'))
        if len(failed_elems) > 0:
            for failed_elem in failed_elems:
                print(f'Soft Displayed Failed, Elements which have failed: {str(failed_elem)}')
            raise AssertionError('Soft Displayed Failed')

