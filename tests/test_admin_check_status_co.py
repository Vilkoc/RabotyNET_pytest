from conftest import app, prep_db
from utilities.db import prepare_db


def test_admin_check_status_co(app, prep_db):
    prepare_db()
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')

    assert app.companies_page.view_status_of_co()
