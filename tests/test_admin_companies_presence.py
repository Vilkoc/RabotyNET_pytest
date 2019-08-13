from conftest import app


def test_admin_companies_presence(app):
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')

    assert app.companies_page.companies_are_visible()
