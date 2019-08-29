"""This module allows you to view vacancies"""
import allure
from data_tests import guest_data


@allure.feature("Vacancies page")
def test_vacancies(app):
    """View vacancies page"""
    with allure.step('Go to vacancies page'):
        app.vacancies_page.view_details()

    with allure.step('View details of vacancy'):
        details = app.vacancies_page.details_text()
        assert details == guest_data.VAC_NAME

    with allure.step('Click button "next"'):
        app.vacancies_page.click_pagination_next()

    with allure.step('Check assertion of button "next"'):
        click_next = app.vacancies_page.next_click_test()
        assert click_next == guest_data.TOP_VACANCY

    with allure.step('Click button "previous"'):
        app.vacancies_page.click_pagination_previous()

    with allure.step('Check assertion of button "previous"'):
        previous = app.vacancies_page.previous_click_test()
        assert previous == guest_data.VAC_NAME
