import pytest
from conftest import app


@pytest.mark.skip(reason = 'skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
def test_block_co(app, make_screen):
    app.header.select_option('Log in')
    app.sign_in_page.login('ADMIN')

    app.companies_page.block_co()

    assert app.companies_page.confirm_with_popup() == "Company blocked"

