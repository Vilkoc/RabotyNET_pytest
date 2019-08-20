from data_tests import guest_data
import allure


@allure.feature("Vacancies page")
def test_vacancies(app, make_screen):
    with allure.step('Go to vacancies page'):
        app.vacancies_page.view_details()

    with allure.step('View details of vacancy'):
        text1 = app.vacancies_page.details_text()
        assert text1 == guest_data.TOP_VACANCY

    with allure.step('Click button "next"'):
        app.vacancies_page.click_pagination_next()

    with allure.step('Check assertion of button "next"'):
        text2 = app.vacancies_page.next_click_test()
        assert text2 == guest_data.TOP_VACANCY

    with allure.step('Click button "previous"'):
        app.vacancies_page.click_pagination_previous()

    with allure.step('Check assertion of button "previous"'):
        text3 = app.vacancies_page.previous_click_test()
        assert text3 == guest_data.TOP_VACANCY
