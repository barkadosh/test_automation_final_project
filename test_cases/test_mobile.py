import allure

import pytest
from utilities.enums import Save, Direction
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class TestMobile:
    @allure.title("TC01: Verify mortgage repayment")
    @allure.description("This test verify the mortgage repayment")
    @pytest.mark.sanity
    def test_verify_mortgage_repayment(self):       # This test will fail
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.NO)
        MobileFlows.verify_mortgage_repayment('17.94')

    @allure.title("TC02: Verify saved details")
    @allure.description("This test verify saved transaction")
    @pytest.mark.sanity
    def test_verify_saved_details(self):
        MobileFlows.mortgage_flow('5000', '8', '3', Save.YES)
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.YES)
        MobileFlows.swipe_screen(Direction.LEFT)
        MobileFlows.verify_rate('3.0')

    @allure.title("TC03: Delete saved transaction")
    @allure.description("this test delete the saved transaction and verify it deleted")
    @pytest.mark.sanity
    def test_delete_saved_trans(self):
        MobileFlows.delete_saved_trans()
        MobileFlows.verify_trans_is_deleted('59.36')
        MobileFlows.delete_saved_trans()


# ~~~ My test cases ~~~

