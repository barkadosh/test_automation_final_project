import subprocess
import time

import mysql.connector

import pytest
import allure

# Selenium
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
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


@pytest.fixture(scope="class")
def init_web_driver(request):
    process = subprocess.Popen(get_data('GrafanaPath'))       # Starting Grafana server
    time.sleep(2)
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
    process.terminate()
    driver.quit()
    if get_data("ExecuteApplitools").lower() == 'yes':
        eyes.close()  # Applitools
        eyes.abort()  # Applitools


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
    driver.quit()@pytest.fixture(scope="class")

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

@pytest.fixture(scope="class")
def init_db_connector(request):
    db_connector = mysql.connector.connect(
        host = get_data('DBHost'),
        database = get_data('DBName'),
        user = get_data('DBUser'),
        password = get_data('DBPassword')
    )
    globals()['db_connector'] = db_connector
    request.cls.db_connector = db_connector
    yield
    db_connector.close()



def get_web_driver():
    web_driver = get_data('Browser')
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


def get_mobile_driver():
    if get_data('Mobile_Device').lower() == 'android':
        driver = get_android(get_data('Udid_Android'))
    elif get_data('Mobile_Device').lower() == 'ios':
        driver = get_ios(get_data('Udid_ios'))
    else:
        driver = None
        raise Exception("Wrong input, unrecognized mobile OS")
    return driver

def get_electron_driver():
    options = selenium.webdriver.ChromeOptions()
    options.binary_location = get_data("Electron_App")
    driver = selenium.webdriver.Chrome(chrome_options=options, executable_path=get_data("Electron_Driver"))
    return driver

def get_desktop_driver():
    dc['app'] = get_data('ApplicationName')
    dc['platformName'] ='Windows'
    dc['deviceName'] = 'WindowsPC'
    driver = appium.webdriver.Remote(get_data('WinAppDriverService'), dc)
    return driver


def get_chrome():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4.x
    return chrome_driver


def get_firefox():
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))  # Selenium 4.x
    return firefox_driver


def get_edge():
    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))  # Selenium 4.x
    return edge_driver


def get_android(udid):
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', dc)
    return android_driver


def get_ios(udid):
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', dc)
    return ios_driver


# catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if it is None - > this is exception from API test
            image = get_data('ScreenshotPath') + f'screen_{str(get_time_stamp())}.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
