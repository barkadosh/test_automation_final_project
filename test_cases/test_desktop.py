import time

import allure

import pytest
from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows

# To run winappdriver:  WIN-key+R: C:\Program Files (x86)\Windows Application Driver\WinAppDriver.exe
# python -m pytest test_desktop.py -s -v --alluredir=../allure-results

# This test cases test the functionality of a uk Mortgage Calculator app
@pytest.mark.usefixtures('init_desktop_driver')
class TestDesktopApp:
    @allure.title("TC01: Adding 2 numbers")
    @allure.description("This test adds 2 numbers and verify the result")
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow("1+7")
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '8')

    @allure.title("TC02: Arithmetic Actions")
    @allure.description("This test does arithmetic actions and verify")
    def test_arithmetic_actions(self):
        DesktopFlows.calculate_flow('2*5+50/2-25')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '5')

    @allure.title("TC03: Validate history list equations")
    @allure.description("Validate equations appears in history list and the last equation appears on top of the list")
    def test_history_validation(self):
        equation = '1+7'
        DesktopFlows.calculate_flow(equation)
        DesktopFlows.clear_flow()
        Verifications.verify_equals(DesktopFlows.get_history_value().text,'1 + 7= 8')
        equation = '3+9'
        DesktopFlows.calculate_flow(equation)
        DesktopFlows.clear_flow()
        Verifications.verify_equals(DesktopFlows.get_history_value().text, '3 + 9= 12')

    @allure.title("TC04: Retrieve equation from history list")
    @allure.description("Validate equations appears in history list and the last equation appears on top of the list")
    def test_history_validation(self):
        equation = '1+7'
        DesktopFlows.calculate_flow(equation)
        DesktopFlows.clear_flow()


    @allure.title("TC05: Clear history list")
    @allure.description("Verify history list is empty after clicking on clear")
    def test_clear_history_validation(self):
        equation = '1+7'
        DesktopFlows.calculate_flow(equation)
        DesktopFlows.clear_flow()
        Verifications.is_exist(DesktopFlows.clear_history())



    def teardown_methode(self):
        DesktopFlows.clear_flow()



# ~~~ My test cases ~~~
# Validate equation saved in history
# Display result from history
# Delete history