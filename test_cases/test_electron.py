import time

import pytest
import allure
from extensions.verifications import Verifications
from workflows.electron_flows import ElectronFlows

# python -m pytest test_electron.py -s -v --alluredir=../allure-results
@pytest.mark.usefixtures('init_electron_driver')
class TestElectron:
    @allure.title("TC01: Add and verify new task")
    @allure.description("Add new task to the electron app and verify 1 task was added")
    def test_add_and_verify_task(self):
        ElectronFlows.add_new_task_flow('Test1')
        time.sleep(2)
        Verifications.verify_equals(ElectronFlows.get_number_of_task_flow(),1)
    @allure.title("TC02: Add and verify new tasks")
    @allure.description("Add 3 new task to the electron app and verify 3 task was added")
    def test_add_and_verify_tasks(self):
        ElectronFlows.add_new_task_flow('Test2')
        ElectronFlows.add_new_task_flow('Test3')
        ElectronFlows.add_new_task_flow('Test4')
        Verifications.verify_equals(ElectronFlows.get_number_of_task_flow(),4)
    def teardown_method(self):
        ElectronFlows.delete_all_tasks_flow()
        time.sleep(2)


# ~~~ My test cases ~~~



    