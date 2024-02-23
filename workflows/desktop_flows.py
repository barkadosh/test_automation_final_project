import allure

from extensions.ui_actions import UiActions
import utilities.manage_pages as page


class DesktopFlows:

    @staticmethod
    @allure.step('Calculate equation')
    def calculate_flow(equation):
        for i in equation:  # example equation: 1+9-5*100
            DesktopFlows.calculator_click(i)
        UiActions.click(page.standard_calc.get_equals())

    @staticmethod
    def calculator_click(value):
        if value == '0':
            UiActions.click(page.standard_calc.get_zero())
        elif value == '1':
            UiActions.click(page.standard_calc.get_one())
        elif value == '2':
            UiActions.click(page.standard_calc.get_two())
        elif value == '3':
            UiActions.click(page.standard_calc.get_three())
        elif value == '4':
            UiActions.click(page.standard_calc.get_four())
        elif value == '5':
            UiActions.click(page.standard_calc.get_five())
        elif value == '6':
            UiActions.click(page.standard_calc.get_six())
        elif value == '7':
            UiActions.click(page.standard_calc.get_seven())
        elif value == '8':
            UiActions.click(page.standard_calc.get_eight())
        elif value == '9':
            UiActions.click(page.standard_calc.get_nine())
        elif value == '+':
            UiActions.click(page.standard_calc.get_plus())
        elif value == '-':
            UiActions.click(page.standard_calc.get_minus())
        elif value == '*':
            UiActions.click(page.standard_calc.get_mult())
        elif value == '/':
            UiActions.click(page.standard_calc.get_divide())
        else:
            raise Exception('Invalid Input')

    @staticmethod
    @allure.step("Get calculator result")
    def get_result_flow():
        result = page.standard_calc.get_result().text.replace("Display is",
                                                              "").strip()  # strip get rid of spaces before and after the text
        return result

    @staticmethod
    @allure.step("Clear calculator result")
    def clear_flow():
        UiActions.click(page.standard_calc.get_clear())

    @staticmethod
    @allure.step("Get history list web element")
    def get_history_value():
        history_value = page.standard_calc.get_history_values(0)
        return history_value


    @staticmethod
    @allure.step("clear and get history list web element")
    def clear_history():
        UiActions.click(page.standard_calc.get_clear_history())
        history_list = page.standard_calc.get_cleared_history_list()
        return history_list









