import allure

import pytest
from extensions.verifications import Verifications
from workflows.desktop_flows import DesktopFlows


# python -m pytest test_electron.py -s -v --alluredir=../allure-results
@pytest.mark.usefixtures('init_desktop_driver')
class TestElectron:
    @allure.title("TC01: Adding 2 numbers")
    @allure.description("This test adds 2 numbers and verify the result")
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow("1+7")
        Verifications.verify_equals(DesktopFlows.get_result_flow(),'8')
