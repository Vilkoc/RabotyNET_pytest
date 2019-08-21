'''This module allows you to automate the updating of the company name'''
import allure
from data_tests.cowner_data import CownerData


@allure.feature("Updating of the company name")
def test_update_company_name(app, make_screen):
    '''Updating of the company name'''

    with allure.step("Login"):
        app.header.select_option(CownerData.OPTION)
        app.sign_in_page.login(CownerData.PERSON)
    with allure.step("Click 'My companies' on the header"):
        app.header.click_my_companies()
    with allure.step("Click 'Update' button near the company name"):
        app.my_companies_page.click_update(CownerData.COMPANY_FOR_UDATING)
    with allure.step("Updating of the name"):
        app.update_company_page.update_company_name(CownerData.COMPANY_RENAME)
        app.update_company_page.click_update_company_button()
    with allure.step("Check the result"):
        app.my_companies_page.click_update(CownerData.COMPANY_RENAME)
        assert app.update_company_page.check_company_name() == CownerData.COMPANY_RENAME
