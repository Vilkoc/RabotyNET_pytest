"""This module contains project fixtures"""
import pytest
import allure
from application import Application
from driver_wrapper import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from utilities.db import prepare_db
from allure_commons.types import AttachmentType
from utilities.db import restart_tomcat


@pytest.fixture(scope='session', autouse=True)
def prep_db(worker_id):
    """Prepares DB for running"""
    if worker_id == 'gw0' or worker_id == 'master':
        prepare_db()


@pytest.fixture(scope='function')
def browser_init():
    """Initiation of webdriver"""
    driver = WebdriverSelection().get_webdriver(WEBDRIVER)
    driver.maximize_window()
    driver.get(URL)
    browser = DriverWrapper(driver, TIMEOUT)
    return browser


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Helper function to obtain test run status"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='function')
def app(browser_init, request):
    """Instantiation of all pages"""
    selenium_test_base = Application(browser_init)

    def teardown():
        if request.node.rep_call.failed:
            allure.attach(browser_init.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        browser_init.driver.quit()

    request.addfinalizer(teardown)
    return selenium_test_base


@pytest.fixture(scope='function')
def get_to_user_profile(app):
    """Transfers to user profile page"""
    app.header.select_option('Log in')
    app.sign_in_page.login('USER')
    app.header.select_option('Profile')


@pytest.fixture(scope='session')
def restart_tomcat_func(request):
    def restart():
        restart_tomcat()

    request.addfinalizer(restart)
