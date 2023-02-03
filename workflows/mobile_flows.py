import allure
from extensions.mobile_actions import MobileActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from test_cases import conftest as conf
from utilities.common_ops import get_data


class MobileFlows:
    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def mortgage_flow(amount, term, rate, save):
        MobileActions.update_text(page.mobile_calculator.get_amount(), amount)
        MobileActions.update_text(page.mobile_calculator.get_term(), amount)
        MobileActions.update_text(page.mobile_calculator.get_rate(), amount)
        MobileActions.click(page.mobile_calculator.get_calculate())
        if save:
            MobileActions.click(page.mobile_calculator.get_save())

    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def verify_mortgage_repayment(expected):
        actual = page.mobile_calculator.get_repayment().text
        # £ - Press and hold the ALT key and type the number 0163 to make a Pound symbol
        Verifications.verify_equals(actual, '£' + expected)

    @staticmethod
    @allure.step('Swipe the page')
    def swipe_screen(direction):
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']

        start_x = None
        start_y = None
        end_x = None
        end_y = None

        if direction == 'left':
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = end_y = height * 0.5
        if direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height * 0.5
        if direction == 'up':
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width * 0.5
        if direction == 'down':
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width * 0.5
        MobileActions.swipe(start_x, start_y, end_x, end_y, int(get_data('Swipe_Duration')))

    @staticmethod
    @allure.step('Verify rate in saved transactions')
    def verify_rate(expected):
        actual = page.mobile_save.get_rate().text
        Verifications.verify_equals(actual, expected + '%')

    @staticmethod
    @allure.step('Delete saved transaction')
    def delete_saved_trans():
        MobileActions.tap(page.mobile_save.get_delete())
        MobileActions.tap(page.mobile_save.get_confirm_delete())