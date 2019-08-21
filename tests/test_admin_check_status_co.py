"""This module allows you to automate creation of claim"""


def test_admin_check_status_co(app, make_screen):
    """ Test-case that check that status of company visible"""
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')

    assert app.companies_page.view_status_of_co()
