from data_tests.cowner_data import CownerData
import allure


@allure.feature("Creation of the company")
def test_create_company(app):
    with allure.step("Login"):
        app.header.select_option(CownerData.OPTION)
        app.sign_in_page.login(CownerData.PERSON)
    with allure.step("Click 'Create company' on the header"):
        app.header.click_create_company()
    with allure.step("Enter company data"):
        app.create_company_page.enter_data(CownerData.COMPANY_DATA)
        app.create_company_page.click_create_button()
    with allure.step("Read company data"):
        app.header.click_my_companies()
        app.my_companies_page.click_update(CownerData.COMPANY_CREATE)
        company_data = app.create_company_page.read_data()
    with allure.step("Check the result"):
        num_of_data = 0
        for data in CownerData.COMPANY_DATA:
            assert data == company_data[num_of_data]
            num_of_data += 1
