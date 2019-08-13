from data_tests.cowner_data import CownerData


def test_update_company_name(app):

    app.header.select_option(CownerData.OPTION)
    app.sign_in_page.login(CownerData.PERSON)
    app.header.click_my_companies()
    app.my_companies_page.click_update(CownerData.COMPANY_FOR_UDATING)
    app.update_company_page.update_company_name(CownerData.COMPANY_RENAME)
    app.update_company_page.click_update_company_button()
    app.my_companies_page.click_update(CownerData.COMPANY_RENAME)
    co_name = app.update_company_page.check_company_name()
    assert co_name == CownerData.COMPANY_RENAME




