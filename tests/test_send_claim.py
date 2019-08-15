import allure


@allure.feature('Sending claim')
def test_send_claim(app, prep_db):
    with allure.step('Log in as user'):
        app.header.select_option('Log in')
        app.sign_in_page.login('USER')

    with allure.step('Go to all vacancy page'):
        app.header.go_to_allVacancies()

    with allure.step('View vacancy details'):
        app.vacancies_page.click_viewDetails_button()

    with allure.step('View company details'):
        app.view_vacancy_page.click_showCompany_button()

    with allure.step('Creating claim'):
        app.view_company_page.click_claim_button()
        with allure.step('Choosing title'):
            app.view_company_page.choose_option()
        with allure.step('Fill out description'):
            app.view_company_page.fill_out_description_field('description')

    with allure.step('Send claim'):
        app.view_company_page.click_send_claim_button()

    with allure.step('Log out'):
        app.header.select_option('Log out')

    with allure.step('Log in as admin'):
        app.header.select_option('Log in')
        app.sign_in_page.login("ADMIN")

    with allure.step('Check result'):
        app.companies_page.click_show_claims_button()
        assert app.companies_page.find_description('description')
