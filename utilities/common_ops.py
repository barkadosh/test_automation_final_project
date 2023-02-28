import csv
import time
import socket

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf
import xml.etree.ElementTree as ET

hostname = socket.gethostname()
print("Hostname:", hostname)

if hostname == 'BarLaptop':
    root_path = 'C:/Automation/Final_Proj_Aut_Py/configuration/data.xml'
elif hostname == 'BarDesktop':
    root_path = 'C:/Automation/test_automation_final_project/configuration/data.xml'


# Connectivity to XML file
def get_data(node_name):
    root = ET.parse(root_path).getroot()
    return root.find('.//' + node_name).text

# Connectivity to CSV file
def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


# Wait conditions
def wait(for_element, elem):
    if for_element == 'element_exist':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))

    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))


def get_time_stamp():
    return time.time()

# Enums

# Enum for selecting displayed element, exist element, etc.. my wait methode (in this file) use this enum
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'


# Enum for selecting from users list in users page by username or by index, "open_user_settings" web flow use this Enum
class By:
    USER = 'user'
    INDEX = 'index'


# Enum for tc- "test_verify_mortgage_repayment" in test_mobile, yes - for saving mortgage repayment, no - for not
class Save:
    YES = True
    NO = False

# Enum for tc- "test_verify_mortgage_repayment" in test_mobile, yes - for saving mortgage repayment, no - for not
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'
