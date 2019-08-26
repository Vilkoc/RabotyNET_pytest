"""This module allows you to automate deleting of the company"""
import allure
from data_tests.cowner_data import CownerData


@allure.feature("Deleting of the company")
def test_delete_company(app, make_screen):
    """Deleting of the company"""

    with allure.step("Login"):
        app.header.select_option(CownerData.OPTION)
        app.sign_in_page.login(CownerData.PERSON)
    with allure.step("Click the 'All companies' on the header"):
        app.header.click_my_companies()
    with allure.step("Delete the company "):
        app.my_companies_page.click_company_delete(CownerData.COMPANY_DELETE)
    with allure.step("Check the result"):

        a =app.my_companies_page.check_company_absence(CownerData.COMPANY_DELETE)

        assert a