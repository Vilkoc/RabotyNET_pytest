import pytest
from application import Application
from driver_wrapper import DriverWrapper
from driver_selection import WebdriverSelection
from config import URL, TIMEOUT, WEBDRIVER
from utilities.db import prepare_db
import allure
from allure_commons.types import AttachmentType


@pytest.fixture(scope='session', autouse=True)
def prep_db(worker_id):
    if worker_id == 'gw0' or worker_id == 'master':
        prepare_db()


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


@pytest.fixture(scope='function')
def get_to_user_profile(app):
    app.header.select_option('Log in')
    app.sign_in_page.login('USER')
    app.header.select_option('Profile')


@pytest.fixture(scope='function')
def make_screen(browser_init, request):
    fails = request.session.testsfailed

    def screen():
        if request.session.testsfailed - fails:
            allure.attach(browser_init.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)

    request.addfinalizer(screen)
    return make_screen
