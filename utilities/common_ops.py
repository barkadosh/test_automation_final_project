import csv
import time
import socket

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET

# To run the automation from different machines - set the root path to the xml configuration file
hostname = socket.gethostname()
print("Hostname:", hostname)

if hostname == 'BarLaptop':
    root_path = 'C:/Automation/Final_Proj_Aut_Py/configuration/data.xml'
elif hostname == 'DESKTOP-TNCSURL':
    root_path = 'C:/Automation/test_automation_final_project/configuration/data.xml'
elif hostname == 'LP-BARK-51XN8S3':
    root_path = 'C:/Users/BarKadosh-Cello/PycharmProjects/test_automation_final_project/configuration/data.xml'


###########################################
# Function Name: get_data
# Function Description: This function reads data from external xml file
# Function Parameters: String - the node name
# Function Return: String - the node value
###########################################
def get_data(node_name):
    root = ET.parse(root_path).getroot()
    return root.find('.//' + node_name).text


###########################################
# Function Name: read_csv
# Function Description: This function reads data from external csv file
# Function Parameters: String - file_name
# Function Return: String - data
###########################################
def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data


###########################################
# Function Name: wait
# Function Description: Explicitly Wait for a web element - this function get the wait time from the config file,
# and wait for the appearance of the web element
# Function Parameters: String(Enum) - for_element , Web element - elem
# Documentation:
# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html?highlight=expected
###########################################
def wait(for_element, elem):
    if for_element == 'element_exist':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))

    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.visibility_of_element_located((elem[0], elem[1])))

    elif for_element == 'element_to_be_clickable':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.element_to_be_clickable((elem[0], elem[1])))


###########################################
# Function Name: wait_for_element_text
# Function Description: Explicitly Wait for a web element text - this function get the wait time from the config file,
# and wait for the text of the web element
# Function Parameters: String(Enum) - for_element , Web element - elem, text - String
###########################################
def wait_for_element_text(for_element, elem, text):
    if for_element == 'text_present_in_element':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(
            EC.text_to_be_present_in_element((elem[0], elem[1]), text))


###########################################
# Function Name: get_time_stamp
# Function Description: This function get the time stamp for the file name of the allure screenshots
# Function Return: Flot - time stamp
###########################################
def get_time_stamp():
    return time.time()


###########################################
# Function Name: save_screenshot()
# Function Description: This function save screenshots to allure report at the end of some of the test cases
###########################################
def save_screenshot():
    image = get_data('ScreenshotPath') + f'screen_{str(get_time_stamp())}.png'
    conf.driver.get_screenshot_as_file(image)
    allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
