import allure
from extensions.mobile_actions import MobileActions
import utilities.manage_pages as page


class MobileFlows:
    @staticmethod
    @allure.step('Fill in mortgage details flow')
    def mortgage_flow(amount, term, rate, save):
        MobileActions.update_text(page.mobile_calculator.get_amount(), amount)
        MobileActions.update_text(page.mobile_calculator.get_term(), amount)
        MobileActions.update_text(page.mobile_calculator.get_rate(), amount)
        MobileActions.click(page.mobile_calculator.get_calculate())
