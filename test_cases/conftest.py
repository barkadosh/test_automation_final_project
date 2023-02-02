import time

import allure
import appium
import selenium
from applitools.selenium import Eyes

from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

import pytest
from selenium import webdriver
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.manage_pages import ManagePages

driver = None
action = None
eyes = Eyes()  # Applitools


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
    ManagePages.init_web_pages()
    if get_data("ExecuteApplitools").lower() == 'yes':
        eyes.api_key = get_data("ApplitoolsAPI")
    yield
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
    ManagePages.init_mobile_pages()
    yield
    driver.quit()


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
        driver = get_android(get_data('Udid'))
    elif get_data('Mobile_Device').lower() == 'ios':
        driver = get_ios(get_data('Udid'))
    else:
        driver = None
        raise Exception("Wrong input, unrecognized mobile OS")


def get_chrome():
    chrome_driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4.x
    return chrome_driver


def get_firefox():
    firefox_driver = selenium.webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))  # Selenium 4.x
    return firefox_driver


def get_edge():
    edge_driver = selenium.webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))  # Selenium 4.x
    return edge_driver


def get_android(udid):
    dc = {}
    dc['udid'] = udid
    dc['appPackage'] = get_data('App_Package')
    dc['appActivity'] = get_data('App_Activity')
    dc['platformName'] = 'android'
    android_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return android_driver


def get_ios(udid):
    dc = {}
    dc['udid'] = udid
    dc['bundle_id'] = get_data('Bundle_ID')
    dc['platformName'] = 'ios'
    ios_driver = appium.webdriver.Remote(get_data('Appium_Server'), dc)
    return ios_driver



# catch exceptions and errors
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:  # if it is None - > this is exception from API test
            image = get_data('ScreenshotPath') + f'screen_{str(get_time_stamp())}.png'
            globals()['driver'].get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
