"""This module allows you to automate visibility of companies"""
import allure


@allure.story('Admin features')
def test_admin_companies_presence(app):
    """ Test-case that check visibility of companies"""
    with allure.step('Log in'):
        app.header.select_option('Log in')
        app.sign_in_page.login('ADMIN')
    with allure.step('Check if companies visible'):
        assert app.companies_page.companies_are_visible()
