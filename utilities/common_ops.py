from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf


def wait(for_element, elem):
    if for_element == 'element_exist':
        WebDriverWait(conf.driver, 5).until(EC.presence_of_element_located((elem[0], elem[1])))

    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, 5).until(EC.visibility_of_element_located((elem[0], elem[1])))


# Enum for selecting displayed element or exist element, my wait methode use this enum
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'
