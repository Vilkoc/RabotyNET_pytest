import pytest
from application import Application
from wrapper import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from utilities.db import prepare_db


@pytest.fixture(scope='function')
def browser_init():
    driver = WebdriverSelection().get_webdriver(WEBDRIVER)
    driver.maximize_window()
    driver.get(URL)
    browser = DriverWrapper(driver, TIMEOUT)
    return browser


@pytest.fixture(scope='function')
def app(browser_init):
    selenium_test_base = Application(browser_init)
    yield selenium_test_base
    browser_init.driver.quit()


@pytest.fixture(scope='session', autouse=True)
def prep_db():
    prepare_db()
    print('===============NNNNNN================')
