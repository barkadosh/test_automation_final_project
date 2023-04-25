import allure

import pytest
from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows


# This automated tests works only on Windows 10!!! - No computability yet with Windows 11
# python -m pytest test_desktop.py -s -v --alluredir=../allure-results

@pytest.mark.usefixtures('init_desktop_driver')
class TestDesktopApp:
    @allure.title("TC01: Adding 2 numbers")
    @allure.description("This test adds 2 numbers and verify the result")
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow("1+7")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '8')

    @allure.title("TC0: Arithmetic Actions")
    @allure.description("This test does arithmetic actions and verify")
    def test_arithmetic_actions(self):
        DesktopFlows.calculate_flow('2*5+50/2-25')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '5')

    def teardown_methode(self):
        DesktopFlows.clear_flow()


# ~~~ My test cases ~~~
