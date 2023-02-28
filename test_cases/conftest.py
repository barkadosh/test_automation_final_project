import pytest
import allure

# Selenium
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
dc = {}

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
    request.cls.action = globals()['action']
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
