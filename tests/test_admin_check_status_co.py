"""This module allows you to automate creation of claim"""
import allure


@allure.story('Admin features')
def test_admin_check_status_co(app, make_screen):
    """ Test-case that check that status of company visible"""
    with allure.step('Log in'):
        app.header.select_option('Log in')
        app.sign_in_page.login('ADMIN')
    with allure.step('Find status of company'):
        assert app.companies_page.view_status_of_co()
