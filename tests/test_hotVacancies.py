from data_tests import guest_data
import allure


@allure.feature("HotVacancies page")
def test_hot_vacancies(app, make_screen):
    with allure.step('Go to hot vacancies page'):
        app.hot_vacancies_page.view_details()

    with allure.step('View details of vacancy'):
        text1 = app.hot_vacancies_page.details_text()
        assert text1 == guest_data.TOP_VACANCY

    with allure.step('Click button "next"'):
        app.hot_vacancies_page.check_pagination_next()

    with allure.step('Check assertion of button "next"'):
        text2 = app.hot_vacancies_page.next_test()
        assert text2 == guest_data.TOP_VACANCY

    with allure.step('Click button "previous"'):
        app.hot_vacancies_page.check_pagination_previous()

    with allure.step('Check assertion of button "previous"'):
        text3 = app.hot_vacancies_page.previous_test()
        assert text3 == guest_data.TOP_VACANCY
