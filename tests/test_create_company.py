from data_tests.cowner_data import CownerData


def test_create_company(app):
    app.header.select_option(CownerData.OPTION)
    app.sign_in_page.login(CownerData.PERSON)

    app.header.click_create_company()
    app.create_company_page.enter_data(CownerData.COMPANY_DATA)
    app.create_company_page.click_create_button()
    app.header.click_my_companies()
    app.my_companies_page.click_update(CownerData.COMPANY_CREATE)
    company_data = app.create_company_page.read_data()

    num_of_data = 0
    for data in CownerData.COMPANY_DATA:
        assert data == company_data[num_of_data]
        num_of_data += 1
