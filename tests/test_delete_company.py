from data_tests.cowner_data import CownerData
import allure


@allure.feature("Delete company")
def test_delete_company(app):

    with allure.step("Login"):
        app.header.select_option(CownerData.OPTION)
        app.sign_in_page.login(CownerData.PERSON)
    with allure.step("All companies"):
        app.header.click_my_companies()
    app.my_companies_page.click_company_delete(CownerData.COMPANY_DELETE)
    check = app.my_companies_page.check_company_present(CownerData.COMPANY_DELETE)
    assert check
