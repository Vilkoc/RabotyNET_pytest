"""This module allows you to automate visibility of companies"""


def test_admin_companies_presence(app, make_screen):
    """ Test-case that check visibility of companies"""
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')

    assert app.companies_page.companies_are_visible()
