import time
import pytest
import allure
from extensions.verifications import Verifications
from utilities.common_ops import save_screenshot
from workflows.electron_flows import ElectronFlows
import utilities.manage_pages as page


# python -m pytest test_electron.py -s -v -m run_this --alluredir=../allure-results
@pytest.mark.usefixtures('init_electron_driver')
class TestElectron:
    @allure.title("TC01: Add and verify new task")
    @allure.description("Add new task to the electron app and verify 1 task was added")
    #@pytest.mark.run_this
    def test_add_and_verify_task(self):
        ElectronFlows.add_new_task_flow('Test1')
        time.sleep(2)
        Verifications.verify_equals(ElectronFlows.get_number_of_task_flow(),1)

    @allure.title("TC02: Add and verify new tasks")
    @allure.description("Add 3 new task to the electron app and verify 3 task was added")
    #@pytest.mark.run_this
    def test_add_and_verify_tasks(self):
        ElectronFlows.add_new_task_flow('Test2')
        ElectronFlows.add_new_task_flow('Test3')
        ElectronFlows.add_new_task_flow('Test4')
        Verifications.verify_equals(ElectronFlows.get_number_of_task_flow(),4)

    @allure.title("TC03: Mark task as done")
    @allure.description("Check and uncheck task's completed checkbox")
    # @pytest.mark.run_this
    def test_mark_task_completed(self):
        ElectronFlows.click_task_checkbox(0)
        Verifications.is_displayed(page.electron_task.get_task_done()[0])
        save_screenshot()
        ElectronFlows.click_task_checkbox(0)
        save_screenshot()
        Verifications.is_displayed(page.electron_task.get_task_not_done()[0])

    @allure.title("TC04: Toggle all completed")
    @allure.description("Check and uncheck all tasks to be completed with Toggle All Completed checkbox")
    # @pytest.mark.run_this
    def test_mark_all_tasks_completed(self):
        ElectronFlows.click_toggle_all_completed_checkbox()
        Verifications.soft_assert(page.electron_task.get_task_done())
        save_screenshot()
        ElectronFlows.click_toggle_all_completed_checkbox()
        Verifications.soft_assert(page.electron_task.get_task_not_done())
        save_screenshot()

    @allure.title("TC05: Filter done tasks")
    @allure.description("Mark task as completed and filter the list to display only done tasks and return to all tasks")
    #@pytest.mark.run_this
    def test_filter_to_completed_tasks(self):
        ElectronFlows.click_task_checkbox(0)
        ElectronFlows.click_task_checkbox(1)
        ElectronFlows.filter_tasks_completed()
        Verifications.verify_equals(ElectronFlows.get_number_of_task_flow(), 2)
        save_screenshot()
        ElectronFlows.filter_all_tasks()
        Verifications.verify_equals(ElectronFlows.get_number_of_task_flow(), 4)
        save_screenshot()

    @allure.title("TC06: Delete tasks")
    @allure.description("Delete all tasks in the list of a specific date")
    def test_delete_tasks(self):
        ElectronFlows.delete_all_tasks_flow()

    @allure.title("TC07: Add a task with color")
    @allure.description("Create a task with color mark")
    @pytest.mark.run_this
    def test_create_colored_task(self):
        ElectronFlows.add_colored_task_flow('Colored task')
        save_screenshot()



    def teardown_method(self):
        time.sleep(2)


# ~~~ My test cases ~~~
# Mark task as done - V
# Toggle all completed - V
# Create task with color icon - V



    