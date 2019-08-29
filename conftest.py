import pytest
from allure_commons.types import AttachmentType
from application import Application
from driver_wrapper import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from utilities.db import prepare_db
from utilities.del_from_db import delete_from_vacancy_resume
from utilities.del_from_db import delete_from_claim
import allure


@pytest.fixture(scope='function')
def browser_init():
    driver = WebdriverSelection().get_webdriver(WEBDRIVER)
    driver.maximize_window()
    driver.get(URL)
    browser = DriverWrapper(driver, TIMEOUT)

    return browser


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Helper function to obtain test run status"""
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='function')
def app(browser_init, request):
    selenium_test_base = Application(browser_init)

    def teardown():
        if request.node.rep_call.failed:
            allure.attach(browser_init.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
        browser_init.driver.quit()

    request.addfinalizer(teardown)
    return selenium_test_base


@pytest.fixture(scope='session', autouse='True')
def prep_db():
    delete_from_vacancy_resume()
    delete_from_claim()
