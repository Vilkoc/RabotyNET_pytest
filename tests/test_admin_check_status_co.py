from conftest import app


def test_admin_check_status_co(app):
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')

    assert app.companies_page.view_status_of_co()
