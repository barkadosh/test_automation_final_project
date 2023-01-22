import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.manage_pages import ManagePages

driver = None
action = None
web_driver = 'Chrom'


@pytest.fixture(scope="class")
def init_web_driver(request):
    globals()['driver'] = get_web_driver()
    driver = globals()['driver']
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("http://localhost:3000/")
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()
    yield
    driver.quit()


def get_web_driver():
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


def get_chrome():
    chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))  # Selenium 4.x
    return chrome_driver


def get_firefox():
    firefox_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))  # Selenium 4.x
    return firefox_driver


def get_edge():
    edge_driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))  # Selenium 4.x
    return edge_driver
