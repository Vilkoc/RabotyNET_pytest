"""This module allows you to automate the creation of the company"""
import allure
from data_tests.cowner_data import CownerData


@allure.feature("Creation of the company")
def test_create_company(app, make_screen):
    """Creation of the company"""

    with allure.step("Login"):
        app.header.select_option(CownerData.OPTION)
        app.sign_in_page.login(CownerData.PERSON)
    with allure.step("Click 'Create company' on the header"):
        app.header.click_create_company()
    with allure.step("Enter company data"):
        app.create_company_page.enter_data(CownerData.COMPANY_DATA)
        app.create_company_page.click_create_button()
    with allure.step("Read company data"):
        app.create_company_page.click_my_companies_tab()
        app.my_companies_page.click_update(CownerData.COMPANY_CREATE)
        company_data = app.create_company_page.read_data()
    with allure.step("Check the result"):
        assert company_data == CownerData.COMPANY_DATA
