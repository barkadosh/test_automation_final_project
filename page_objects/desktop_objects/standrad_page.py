from selenium.webdriver.common.by import By

zero = (By.NAME, "Zero")
one = (By.NAME, "One")
two = (By.NAME, "Two")
three = (By.NAME, "Three")
four = (By.NAME, "Four")
five = (By.NAME, "Five")
six = (By.NAME, "Six")
seven = (By.NAME, "Seven")
eight = (By.NAME, "Eight")
nine = (By.NAME, "Nine")
plus = (By.NAME, "Plus")
minus = (By.NAME, "Minus")
mult = (By.NAME, "Multiply by")
divide = (By.NAME, "Divide by")
equals = (By.NAME, "Equals")
result = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
clear = (By.NAME, "Clear")
history_values = (By.XPATH, "//*[@AutomationId='HistoryListView']/*")
clear_history = (By.XPATH, "//*[@AutomationId='ClearHistory']")
cleared_history_list = (By.XPATH, "//*[@AutomationId='HistoryEmpty']")
equation = (By.XPATH, "//*[@AutomationId='CalculatorExpression']")

class StandardPage:

    def __init__(self, driver):
        self.driver = driver

    def get_zero(self):
        return self.driver.find_element(zero[0], zero[1])

    def get_one(self):
        return self.driver.find_element(one[0], one[1])

    def get_two(self):
        return self.driver.find_element(two[0], two[1])

    def get_three(self):
        return self.driver.find_element(three[0], three[1])

    def get_four(self):
        return self.driver.find_element(four[0], four[1])

    def get_five(self):
        return self.driver.find_element(five[0], five[1])

    def get_six(self):
        return self.driver.find_element(six[0], six[1])

    def get_seven(self):
        return self.driver.find_element(seven[0], seven[1])

    def get_eight(self):
        return self.driver.find_element(eight[0], eight[1])

    def get_nine(self):
        return self.driver.find_element(nine[0], nine[1])

    def get_plus(self):
        return self.driver.find_element(plus[0], plus[1])

    def get_minus(self):
        return self.driver.find_element(minus[0], minus[1])

    def get_mult(self):
        return self.driver.find_element(mult[0], mult[1])

    def get_divide(self):
        return self.driver.find_element(divide[0], divide[1])

    def get_equals(self):
        return self.driver.find_element(equals[0], equals[1])

    def get_result(self):
        return self.driver.find_element(result[0], result[1])

    def get_clear(self):
        return self.driver.find_element(clear[0], clear[1])

    def get_history_values(self, i):
        return self.driver.find_elements(history_values[0], history_values[1])[i]

    def get_clear_history(self):
        return self.driver.find_element(clear_history[0], clear_history[1])

    def get_cleared_history_list(self):
        return self.driver.find_element(cleared_history_list[0], cleared_history_list[1])

    def get_equation(self):
        return self.driver.find_element(equation[0], equation[1])



