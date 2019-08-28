import allure


@allure.feature("Search page")
@allure.description("Opisanie")
@allure.story("пошук вакансії")
def test_1search_button(app, make_screen):
    with allure.step('Go to vacancies page'):
        app.search_page.search_button_click()

    with allure.step('Choose criteria'):
        app.search_page.criteria_choose()

    with allure.step('Write key word'):
        app.search_page.key_word_field()

    with allure.step('Start search by filter'):
        app.search_page.start_search_click()

    with allure.step('Check assertion'):
        assert app.search_page.filter_city()
