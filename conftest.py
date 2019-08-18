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
from tests.test_send_resume import test_send_resume


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


@pytest.fixture(scope='session')
def prep_db():
    delete_from_vacancy_resume()
    delete_from_claim()


@pytest.fixture(scope='function')
def make_screen(browser_init, request):
    fails = request.session.testsfailed

    def screen():
        if request.session.testsfailed - fails:
            allure.attach(browser_init.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    request.addfinalizer(screen)
    return make_screen
