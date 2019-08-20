import allure

from conftest import app


@allure.story('Admin features')
def test_admin_companies_presence(app, make_screen):
    with allure.step('Log in'):
        app.header.select_option('Log in')
        app.sign_in_page.login('ADMIN')
    with allure.step('Check if companies visible'):
        assert app.companies_page.companies_are_visible()
