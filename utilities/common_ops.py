from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


# Connectivity to XML file
# From laptop:
# def get_data(node_name):
#     root = ET.parse('C:/Automation/Final_Proj_Aut_Py/configuration/data.xml').getroot()
#     return root.find('.//' + node_name).text
# From desktop:
def get_data(node_name):
    root = ET.parse('C:/Automation/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

# Wait conditions
def wait(for_element, elem):
    if for_element == 'element_exist':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))

    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))


# Enum for selecting displayed element, exist element, etc.. my wait methode use this enum
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'


# Enum for selecting from users list in users page by username or by index, " open_user_settings" web flow use this Enum
class By:
    USER = 'user'
    INDEX = 'index'
