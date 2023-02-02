from selenium.webdriver.common.by import By

amount = (By.ID, "tvAmount")
term = (By.ID, "tvTerm")
rate = (By.ID, "tvRate")
delete = (By.ID, "btnDel")
confirm_delete = (By.XPATH, "//*[@text='OK']")
cancel_confirm_delete = (By.XPATH, "//*[@text='Cancel']")
repayment = (By.ID, "tvRepayment")
interest = (By.ID, "tvInterestOnly")


class SavedPage:
    def __init__(self, driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element(amount[0], amount[1])

    def get_term(self):
        return self.driver.find_element(term[0], term[1])

    def get_rate(self):
        return self.driver.find_element(rate[0], rate[1])

    def get_delete(self):
        return self.driver.find_element(delete[0], delete[1])

    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0], confirm_delete[1])

    def get_cancel_confirm_delete(self):
        return self.driver.find_element(cancel_confirm_delete[0], cancel_confirm_delete[1])

    def get_repayment(self):
        return self.driver.find_element(repayment[0], repayment[1])

    def get_interest(self):
        return self.driver.find_element(interest[0], interest[1])
