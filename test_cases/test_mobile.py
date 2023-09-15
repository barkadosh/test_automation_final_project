import time
import allure
import pytest
from utilities.enums import Save, Direction
from workflows.mobile_flows import MobileFlows

#python -m pytest test_mobile.py -s -v -m run_this --alluredir=../allure-results

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
        #MobileFlows.approve_start_app_messages()
        MobileFlows.mortgage_flow('5000', '8', '3', Save.YES)
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.YES)
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.verify_rate('3.0')

    @allure.title("TC03: Negative test - Verify transaction is deleted")
    @allure.description("this test verify transaction deleted transaction doesn't appears in the app")
    @pytest.mark.sanity
    def test_delete_saved_trans(self):
        #MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.delete_saved_trans()
        MobileFlows.verify_trans_is_deleted('59.36')
        MobileFlows.delete_saved_trans()

    # ~~~ My test cases ~~~

    @allure.title("TC04: Verify mortgage details")
    @allure.description("this test Verify amount, yrs, percentage, repayment, interest are the same in the calculator "
                        "and in the saved transaction")
    def test_mortgage_details(self):
        MobileFlows.swipe_screen(Direction.RIGHT)
        MobileFlows.mortgage_flow('1000', '10', '10', Save.YES)
        MobileFlows.compare_transaction_details('1000', '10', '10')
        MobileFlows.delete_saved_trans()

    @allure.title("TC05: Verify transaction date and hour")
    @allure.description("this test Verify that transaction saved on the current date and hour")
    @pytest.mark.run_this
    def test_verify_time(self):
        #MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.mortgage_flow('1000', '10', '10', Save.YES)
        MobileFlows.check_current_time()
        MobileFlows.swipe_screen(Direction.RIGHT)
        # 10-09-2023
        # 20:04:28

    @allure.title("TC04: Verify mortgage details")
    @allure.description("this test Verify amount, yrs, percentage, repayment, interest are the same in the calculator "
                        "and in the saved transaction")
    @pytest.mark.run_this
    def test_mortgage_details(self):
        MobileFlows.swipe_screen(Direction.RIGHT)
        MobileFlows.mortgage_flow('1000', '10', '10', Save.YES)

        MobileFlows.swipe_screen(Direction.LEFT)



    def teardown_method(self):
        time.sleep(1)

# Test 1: Verify amount, yrs, percentage, repayment, interest are the same in the calculator and in the saved transaction
# Test 2: Verify that the date and hour of the transaction is saved on are the current time
# Test 3: Verify the calculation is correct = amount*(1+precetage)/yrs
