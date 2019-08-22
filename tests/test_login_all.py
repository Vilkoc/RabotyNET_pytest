"""Checks login for all persons: admin, cowner, user"""
import allure
from credentials import Credentials
import pytest


@allure.feature('Login all users')
@pytest.mark.parametrize('person', Credentials.keys())
def test_login_all(app, person):
    """Reads person credentials and tries to login for all types of persons"""
    with allure.step('Check log in for all'):
        app.header.select_option('Log in')
        app.sign_in_page.login(person)
        assert app.header.person_verify(person)
        app.header.select_option('Log out')
