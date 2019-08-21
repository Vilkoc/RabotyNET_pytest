from credentials import Credentials
import pytest
import allure

@allure.feature('Login all users')
@pytest.mark.parametrize('person', Credentials.keys())
def test_login_all(app, person):
    with allure.step('Check log in for all'):
        app.header.select_option('Log in')
        app.sign_in_page.login(person)
        assert app.header.person_verify(person)
        app.header.select_option('Log out')






