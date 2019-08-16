import allure


@allure.feature('Changing data')
def test_change_data(app):
    with allure.step('Log in'):
        app.header.select_option('Log in')
        app.sign_in_page.login('USER')

    with allure.step('Go to all vacancy page'):
        app.header.go_to_allVacancies()

    with allure.step('View vacancy details'):
        app.vacancies_page.click_viewDetails_button()

    with allure.step('Go to preview resume page'):
        app.view_vacancy_page.click_sendResume_button()

    with allure.step('Go to changing resume'):
        app.preview_resume_page.click_change_button()

    with allure.step('Changing resume'):
        app.edit_resume_page.change_positionField('Middle Developer')
        app.edit_resume_page.click_previewPDF_button()

    with allure.step('Check result'):
        app.preview_resume_page.click_change_button()
        text = app.edit_resume_page.confirmation_changes()
        assert text == 'Middle Developer'

