import allure
import pytest

import page_objects.mobile_objects.calculator_page
from extensions.mobile_actions import MobileActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from test_cases import conftest as conf
from utilities.common_ops import get_data, wait, read_csv
from utilities.enums import For, Direction


class MobileFlows:
    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def mortgage_flow(amount, term, rate, save):
        MobileActions.update_text(page.mobile_calculator.get_amount(), amount)
        MobileActions.update_text(page.mobile_calculator.get_term(), term)
        MobileActions.update_text(page.mobile_calculator.get_rate(), rate)
        MobileActions.click(page.mobile_calculator.get_calculate())
        wait(For.ELEMENT_DISPLAYED, page_objects.mobile_objects.calculator_page.repayment)
        if save:
            MobileActions.click(page.mobile_calculator.get_save())

    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def verify_mortgage_repayment(expected):
        actual = page.mobile_calculator.get_repayment().text
        Verifications.verify_equals(actual, '£' + expected)  # £ - Press and hold the ALT key and type the number 0163
        # to make a Pound symbol

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

    @staticmethod
    @allure.step('Verify saved transaction is deleted')
    def verify_trans_is_deleted(repayment_amount):
        repayments = page.mobile_save.get_repayment_list()
        for repayment in repayments:
            if repayment == repayment_amount:
                Verifications.is_not_displayed(page.mobile_save.get_repayment())

    # @staticmethod
    # @allure.step('Get transactions details in calculator page')
    # def get_transaction_details(amount, term, rate):
    #     amount_calculator = amount
    #     term_calculator = term
    #     rate_calculator = rate
    #     repayment_calculator = page.mobile_calculator.get_repayment().text
    #     interest_calculator = page.mobile_calculator.get_interest().text
    #     # calc_trans_lst = [amount_calculator, term_calculator, rate_calculator, repayment_calculator, interest_calculator]
    #     # write_to_file('calc_trans', calc_trans_lst)
    #     MobileFlows.swipe_screen(Direction.LEFT)
    #     amount_saved = page.mobile_save.get_amount()
    #     term_saved = page.mobile_save.get_term()
    #     rate_saved = page.mobile_save.get_rate()
    #     repayment_saved = page.mobile_save.get_repayment()
    #     interest_saved = page.mobile_save.get_interest()
    #     # saved_trans_lst = [amount_saved, term_saved, rate_saved, repayment_saved, interest_saved]
    #     # write_to_file('saved_trans', saved_trans_lst)


    # @staticmethod
    # @allure.step('Get transactions details in saved page')
    # def verify_transaction_details_equals():
    #     actual =


# Parameters for "TC04: Verify mortage details" from test_mobile.py, imported from Users_CSV File
data1 = read_csv(get_data('Calc_Trans'))
data2 = read_csv(get_data('Saved_Trans'))
trans_testdata = [
    (data1[0][0], data2[0][0]),
    (data1[1][0], data2[1][0]),
    (data1[2][0], data2[2][0]),
    (data1[3][0], data2[3][0]),
    (data1[4][0], data2[4][0]),
    (data1[5][0], data2[5][0])
    ]
