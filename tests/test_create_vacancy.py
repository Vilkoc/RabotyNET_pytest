from data_tests.cowner_data import CownerData


def test_create_vacancy(app):

    app.header.select_option(CownerData.OPTION)
    app.sign_in_page.login(CownerData.PERSON)

    app.header.click_my_companies()
    app.my_companies_page.click_view_details()
    app.view_company_page.click_create_vacancy()
    app.create_vacancy_page.enter_vacancy_data(CownerData.VACANCY_DATA)
    app.create_vacancy_page.choose_employment()
    app.create_vacancy_page.choose_currency()
    app.create_vacancy_page.click_add_requirement()
    app.create_vacancy_page.enter_requirements(CownerData.REQUIREMENTS)
    app.create_vacancy_page.click_vacancy_create()
    app.view_company_page.view_vacancy_details(CownerData.VACANCY_NAME)
    all_vacancy_data = app.create_vacancy_page.read_vacancy_data()

    num_of_vac_data = 0
    for vac_data in CownerData.VACANCY_DATA:
        assert vac_data == all_vacancy_data[num_of_vac_data]
        num_of_vac_data += 1
