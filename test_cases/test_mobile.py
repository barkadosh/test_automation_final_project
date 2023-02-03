import allure

import pytest
from utilities.common_ops import Save
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures('init_mobile_driver')
class TestMobile:
    @allure.title("TC01: Verify mortgage repayment")
    @allure.description("Verify the mortgage repayment")
    @pytest.mark.sanity
    def test_verify_mortgage_repayment(self):
        MobileFlows.mortgage_flow('1000', '5', '2.5', Save.NO)
        MobileFlows.verify_mortgage_repayment('17.94')