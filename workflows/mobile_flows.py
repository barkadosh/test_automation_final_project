from time import strftime

import allure

import page_objects.mobile_objects.calculator_page
from extensions.mobile_actions import MobileActions
import utilities.manage_pages as page
from extensions.verifications import Verifications
from test_cases import conftest as conf
from utilities.common_ops import get_data, wait, get_current_date, get_current_hour
from utilities.enums import For, Direction


class MobileFlows:

    # @staticmethod
    # @allure.step('Approve start app screens')
    # def approve_start_app_messages():
    #     MobileActions.click(page.mobile_calculator.approve_notif())
    #     MobileActions.click(page.mobile_calculator.alrt_msg_ok())

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

    # Fix structure like current and trans time flows!!!!!!!!
    @staticmethod
    @allure.step('Get transactions details in calculator page')
    def compare_transaction_details(amount, term, rate):
        amount_calculator = '£' + str(float(amount))
        term_calculator = str(float(term)) + ' yrs'
        rate_calculator = str(float(rate)) + '%'
        repayment_calculator = page.mobile_calculator.get_repayment().text
        interest_calculator = page.mobile_calculator.get_interest().text
        actual = [amount_calculator, term_calculator, rate_calculator, repayment_calculator,
                  interest_calculator]
        MobileFlows.swipe_screen(Direction.LEFT)
        amount_saved = page.mobile_save.get_amount().text
        term_saved = page.mobile_save.get_term().text
        rate_saved = page.mobile_save.get_rate().text
        repayment_saved = page.mobile_save.get_repayment().text
        interest_saved = page.mobile_save.get_interest().text
        expected = [amount_saved, term_saved, rate_saved, repayment_saved, interest_saved]
        Verifications.verify_lists_are_equals(actual, expected)

    @staticmethod
    @allure.step('Check current time')
    def check_current_time():
        current_date = get_current_date()
        print(current_date)
        current_time = strftime("%a %b %d %H:%M")
        current_year = strftime("%Y")
        current_strftime = current_time + ' ' + current_year
        print(current_strftime)
        return current_date, current_strftime

    @staticmethod
    @allure.step('Check transaction time')
    def check_trans_time():
        trans_date = page.mobile_save.get_timestamp().text
        current_hour = int(strftime("%H"))
        # Fix for a 1-day diversion between 00:00-02:00
        if 0 <= current_hour <= 2:
            trans_day = int(trans_date[10:11]) + 1
            trans_date = trans_date[0:10] + str(trans_day) + trans_date[11:19]
        print(trans_date)
        trans_strftime = page.mobile_save.get_strftime().text
        trans_strftime = trans_strftime[0:16] + trans_strftime[-5:]
        print(trans_strftime)
        return trans_date, trans_strftime
