"""This module allows send resume to the company"""
import allure
import pytest

@allure.feature('Sending resume')
def test_send_resume(app):
    """Sending resume to the company"""
    with allure.step('Log in as user'):
        app.header.select_option('Log in')
        app.sign_in_page.login('USER')

    with allure.step('Go to all vacancy page'):
        app.header.go_to_all_vacancies()

    with allure.step('View vacancy details'):
        app.vacancies_page.click_view_details_button()

    with allure.step('Go to preview resume page'):
        app.view_vacancy_page.click_send_resume_button()

    with allure.step('Send resume'):
        app.preview_resume_page.click_send_email_button()

    with allure.step('Check result'):
        message = app.preview_resume_page.confirmation_message()
        assert message == "Mail has been sent!"
