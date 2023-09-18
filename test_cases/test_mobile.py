import time
import allure
import pytest
from utilities.enums import Save, Direction
from workflows.mobile_flows import MobileFlows
from extensions.verifications import Verifications


# python -m pytest test_mobile.py -s -v -m run_this --alluredir=../allure-results

@pytest.mark.usefixtures('init_mobile_driver')
class TestMobile:
    @allure.title("TC01: Verify mortgage repayment")
    @allure.description("This test verify that calculated transaction that are not saved"
                        " won't appear in the saved transaction")
    @pytest.mark.sanity
    @pytest.mark.xfail
    def test_verify_mortgage_repayment(self):  # This test will fail
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.NO)
        MobileFlows.verify_mortgage_repayment('17.94')

    @allure.title("TC02: Verify saved rate")
    @allure.description("This test verify saved transaction")
    @pytest.mark.sanity
    def test_verify_saved_details(self):
        # MobileFlows.approve_start_app_messages()
        MobileFlows.mortgage_flow('5000', '8', '3', Save.YES)
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.YES)
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.verify_rate('3.0')
        MobileFlows.delete_saved_trans()

    @allure.title("TC03: Verify transaction is deleted")
    @allure.description("this test verify transaction deleted transaction doesn't appears in the app")
    @pytest.mark.sanity
    def test_delete_saved_trans(self):
        MobileFlows.swipe_screen(Direction.RIGHT)
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.YES)
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.verify_trans_is_deleted('17.94')

    @allure.title("TC04: Verify mortgage details")
    @allure.description("this test Verify amount, yrs, percentage, repayment, interest are the same in the calculator "
                        "and in the saved transaction")
    @pytest.mark.run_this
    def test_mortgage_details(self):
        MobileFlows.swipe_screen(Direction.RIGHT)
        MobileFlows.mortgage_flow('1000', '10', '10', Save.YES)
        MobileFlows.set_transaction_details('1000', '10', '10')
        actual = [MobileFlows.get_transaction_details()[0],
                  MobileFlows.get_transaction_details()[1],
                  MobileFlows.get_transaction_details()[2],
                  MobileFlows.get_transaction_details()[3],
                  MobileFlows.get_transaction_details()[4]]
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.set_saved_transaction_details()
        expected = [MobileFlows.get_saved_transaction_details()[0], MobileFlows.get_saved_transaction_details()[1],
                    MobileFlows.get_saved_transaction_details()[2], MobileFlows.get_saved_transaction_details()[3],
                    MobileFlows.get_saved_transaction_details()[4]]
        Verifications.verify_lists_are_equals(actual, expected)

    @allure.title("TC05: Verify transaction date and hour")
    @allure.description("this test Verify that transaction saved on the current date and hour (not including seconds)")
    def test_verify_time(self):
        MobileFlows.swipe_screen(Direction.RIGHT)
        MobileFlows.mortgage_flow('1000', '10', '10', Save.YES)
        MobileFlows.check_current_time()
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.check_trans_time()
        # Verify saved on message shows the correct date
        Verifications.verify_equals('Saved on ' + MobileFlows.check_current_time()[0],
                                    MobileFlows.check_trans_time()[0])
        # Verify the header full date is correct
        Verifications.verify_equals(MobileFlows.check_trans_time()[1], MobileFlows.check_current_time()[1])

    # @allure.title("TC06: Verify mortgage calculation")
    # @allure.description("this test Verify amount, yrs, percentage, repayment, interest are the same in the calculator "
    #                     "and in the saved transaction")
    # @pytest.mark.run_this
    # def test_mortgage_details(self):
    #     MobileFlows.swipe_screen(Direction.RIGHT)
    #     MobileFlows.mortgage_flow('1000', '10', '10', Save.YES)
    #
    #     MobileFlows.swipe_screen(Direction.LEFT)

    def teardown_method(self):
        MobileFlows.delete_saved_trans()
        time.sleep(1)

# ~~~ My test cases ~~~
# TC04: Verify mortgage details- Verify amount, yrs, percentage, repayment, interest are the same in the calculator and in the saved transaction
# TC05: Verify transaction date and hour- Verify that the date and hour of the transaction is saved on the current time
# TC06: Verify mortgage calculation- Verify the mortgage calculation is correct = amount*(1+precetage)/yrs
