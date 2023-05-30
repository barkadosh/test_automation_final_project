import mysql.connector
import pytest
import allure

# Selenium
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ActionChains
from applitools.selenium import Eyes

# Selenium + Appium
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
from utilities.common_ops import get_data, get_time_stamp

# Appium
import appium
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction

driver = None
action = None
action2 = None
m_action = None
mobile_size = None
db_connector = None
dc = {}

eyes = Eyes()  # Applitools


###########################################
# Function Name: init_web_driver
# Function Description: This function initiate the web driver for the tests cases in test_web.py module
###########################################
@pytest.fixture(scope="class")
def init_web_driver(request):
    if get_data("ExecuteApplitools").lower() == 'yes':
        globals()['driver'] = get_web_driver()
    else:
        edriver = get_web_driver()
        globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(int(get_data('WaitTime')))
    driver.get(get_data('Url'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_web_pages()
    if get_data("ExecuteApplitools").lower() == 'yes':
        eyes.api_key = get_data("ApplitoolsAPI")
    yield
    driver.quit()
    if get_data("ExecuteApplitools").lower() == 'yes':
        eyes.close()  # Applitools
        eyes.abort()  # Applitools


###########################################
# Function Name: init_mobile_driver
# Function Description: This function initiate the mobile driver for the tests cases in test_mobile.py module
###########################################
@pytest.fixture(scope="class")
def init_mobile_driver(request):
    edriver = get_mobile_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = TouchAction(driver)
    request.cls.action = globals()['action']
    globals()['action2'] = TouchAction(driver)
    request.cls.action2 = globals()['action2']
    globals()['m_action'] = MultiAction(driver)
    request.cls.m_action = globals()['m_action']
    globals()['mobile_size'] = driver.get_window_size()
    request.cls.mobile_size = globals()['mobile_size']
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


###########################################
# Function Name: init_electron_driver
# Function Description: This function initiate the electron driver for the tests cases in test_electron.py module
###########################################
@pytest.fixture(scope="class")
def init_electron_driver(request):
    edriver = get_electron_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    request.cls.action = globals()['action']
    ManagePages.init_electron_pages()
    yield
    driver.quit()


###########################################
# Function Name: init_desktop_driver
# Function Description: This function initiate the WinApp driver for the tests cases in test_desktop.py module
###########################################
@pytest.fixture(scope="class")
def init_desktop_driver(request):
    edriver = get_desktop_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver = globals()['driver']
    driver.implicitly_wait(int(get_data('WaitTime')))
    request.cls.driver = driver
    ManagePages.init_desktop_pages()
    yield
    driver.quit()


###########################################
# Function Name: init_db_connector
# Function Description: This function initiate the database connector for the tests cases in test_web_db.py module
###########################################
@pytest.fixture(scope="class")
def init_db_connector(request):
    db_connector = mysql.connector.connect(
        host=get_data('DBHost'),
        database=get_data('DBName'),
        user=get_data('DBUser'),
        password=get_data('DBPassword')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()


###########################################
# Function Name: get_web_driver
# Function Description: This function call the web driver based on the web browser type
# and return it to the init_web_driver function
###########################################
def get_web_driver():
    web_driver = get_data('Browser')   # To choose browser from XML
    # web_driver = os.getenv('Browser')    # To choose browser from Jenkins
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception('Wrong Input, Unrecognized Browser')
    return driver


###########################################
# Function Name: get_mobile_driver
# Function Description: This function call the mobile driver based on the device type
# and return it to the init_mobile_driver function
###########################################
def get_mobile_driver():
    if get_data('Mobile_Device').lower() == 'android':
        driver = get_android(get_data('Udid_Android'))
    elif get_data('Mobile_Device').lower() == 'ios':
        driver = get_ios(get_data('Udid_ios'))
    else:
        driver = None
        raise Exception("Wrong input, unrecognized mobile OS")
    return driver


###########################################
# Function Name: get_electron_driver
# Function Description: This function get the electron driver and return it to the init_electron_driver function
###########################################
def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data("Electron_App")
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data("Electron_Driver"))
    return driver


###########################################
# Function Name: get_desktop_driver
# Function Description: This function get the WinApp driver and return it to the init_desktop_driver function
###########################################
def get_desktop_driver():
    dc['app'] = get_data('ApplicationName')
    dc['platformName'] = 'Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('WinAppDriverService'), dc)
    return driver


###########################################
# Function Name: get_chrome
# Function Description: This function get the chrom webdriver and return it to the get_web_driver function
###########################################
def get_chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": get_data("path_to_download_directory"),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)  # Selenium 4.x

    return chrome_driver


###########################################
# Function Name: get_firefox
# Function Description: This function get the firefox webdriver and return it to the get_web_driver function
###########################################
def get_firefox():
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))  # Selenium 4.x
    return firefox_driver


###########################################
# Function Name: get_edge
# Function Description: This function get the edge webdriver and return it to the get_web_driver function
###########################################
def get_edge():
    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))  # Selenium 4.x
    return edge_driver


###########################################
# Function Name: get_android
# Function Description: This function get the Android driver and return it to the get_mobile_driver function
###########################################
def get_android(udid):
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return android_driver


###########################################
# Function Name: get_android
# Function Description: This function get the IOS driver and return it to the get_mobile_driver function
###########################################
def get_ios(udid):
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return ios_driver


###########################################
# Function Name: pytest_exception_interact
# Function Description: This function catch exceptions and errors and saves a screenshot for allure reports in
# allure-screen-shots folder
###########################################
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if it is None - > this is exception from API test
            image = get_data('ScreenshotPath') + f'screen_{str(get_time_stamp())}.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
