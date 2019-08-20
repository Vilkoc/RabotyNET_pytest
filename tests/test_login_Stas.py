import pytest
import allure

@allure.feature('Sign In')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'Сompanies'),
    ('user@gmail.com', 'user', 'Create company1'),
    ('cowner@gmail.com', 'cowner', 'My companies')
    ])
def test_login_logout(app, make_screen, user, password, expected):
    """ Testcase for user login.
        Try to login for each user"""
    page = app

    page.header.click_icon()
    page.header.click_log_in()

    page.sign_in_page.enter_sign_in_email(user)
    page.sign_in_page.enter_sign_in_password(password)
    page.sign_in_page.click_sign_in()

    with allure.step('Check if user logined'):
        assert page.header.is_logined(), "No 'log out' link"
        page.header.click_icon()

    with allure.step('Check if user authorized'):
        assert page.header.get_text_of_first_link() == expected, 'Wrong link text'

    page.header.click_icon()
    page.header.click_log_out()
