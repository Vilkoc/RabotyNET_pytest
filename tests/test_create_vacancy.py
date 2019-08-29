"""This module allows you to automate the creation of the vacancy"""
import allure
from data_tests.cowner_data import CownerData
import time


@allure.feature("Creation of the vacancy")
def test_create_vacancy(app):
    """Creation of the vacancy"""

    with allure.step("Login"):
        app.header.select_option(CownerData.OPTION)
        app.sign_in_page.login(CownerData.PERSON)
    with allure.step("Click 'My companies' on the header"):
        app.header.click_my_companies()
    with allure.step("Click 'View details' near the company name"):
        app.my_companies_page.click_view_details()
    with allure.step("Click 'Create vacancy'"):
        app.view_company_page.click_create_vacancy()
    with allure.step("Enter vacancy data and save it"):
        app.create_vacancy_page.enter_vacancy_data(CownerData.VACANCY_DATA)
    with allure.step("Choose employment and currency"):
        app.create_vacancy_page.choose_employment()
        app.create_vacancy_page.choose_currency()
    with allure.step("Add requirements"):
        app.create_vacancy_page.click_add_requirement()
        app.create_vacancy_page.enter_requirements(CownerData.REQUIREMENTS)
        time.sleep(1)
        app.create_vacancy_page.click_vacancy_create()
    with allure.step("Read data"):
        app.view_company_page.view_vacancy_details(CownerData.VACANCY_NAME)
        all_vacancy_data = app.create_vacancy_page.read_vacancy_data()
    with allure.step("Check the result"):
        assert all_vacancy_data == CownerData.VACANCY_DATA
