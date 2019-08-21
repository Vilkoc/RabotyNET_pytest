'''This module allows you to view hot vacancies'''
import allure
from data_tests import guest_data


@allure.feature("HotVacancies page")
def test_hot_vacancies(app, make_screen):
    """View hot vacancies page"""
    with allure.step('Go to hot vacancies page'):
        app.hot_vacancies_page.view_details()

    with allure.step('View details of vacancy'):
        details = app.hot_vacancies_page.details_text()
        assert details == guest_data.TOP_VACANCY

    with allure.step('Click button "next"'):
        app.hot_vacancies_page.click_pagination_next()

    with allure.step('Check assertion of button "next"'):
        next = app.hot_vacancies_page.next_click_test()
        assert next == guest_data.TOP_VACANCY

    with allure.step('Click button "previous"'):
        app.hot_vacancies_page.click_pagination_previous()

    with allure.step('Check assertion of button "previous"'):
        previous = app.hot_vacancies_page.previous_click_test()
        assert previous == guest_data.TOP_VACANCY
