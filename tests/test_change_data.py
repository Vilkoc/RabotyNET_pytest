"""This module allows change data in user resume"""
import allure


@allure.feature('Changing data')
def test_change_data(app):
    """Change data in "Position" field"""
    with allure.step('Log in'):
        app.header.select_option('Log in')
        app.sign_in_page.login('USER')

    with allure.step('Go to all vacancy page'):
        app.header.go_to_all_vacancies()

    with allure.step('View vacancy details'):
        app.vacancies_page.click_view_details_button()

    with allure.step('Go to preview resume page'):
        app.view_vacancy_page.click_send_resume_button()

    with allure.step('Go to changing resume'):
        app.preview_resume_page.click_change_button()

    with allure.step('Changing resume'):
        app.edit_resume_page.change_position_field('Middle Developer')
        app.edit_resume_page.click_preview_pdf_button()

    with allure.step('Check result'):
        app.preview_resume_page.click_change_button()
        text = app.edit_resume_page.confirmation_changes()
        assert text == 'Middle Developer'
