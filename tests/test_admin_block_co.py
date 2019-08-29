"""This module allows you to automate company blocking"""
import allure
import pytest


@allure.story('Admin features')
@pytest.mark.skip(reason='skip due to: "https://ssu-jira.softserveinc.com/browse/RAB-86"')
def test_block_co(app):
    """ Test-case to block company"""
    with allure.step('Log in'):
        app.header.select_option('Log in')
        app.sign_in_page.login('ADMIN')
    with allure.step('Block Company'):
        app.companies_page.block_co()

    assert app.companies_page.confirm_with_popup() == "Company blocked"
