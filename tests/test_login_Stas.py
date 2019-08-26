""" This module automate testing for sign in users (user, cowner, admin) """
import pytest
import allure


@allure.feature('Sign In')
@pytest.mark.parametrize('user, password, expected', [
    ('admin@gmail.com', 'admin', 'Сompanies'),
    ('user@gmail.com', 'user', 'Create company'),
    ('cowner@gmail.com', 'cowner', 'My companies')
])
def test_login_logout(app, make_screen, user, password, expected):
    """ Test case for user login.
        Try to login for each user"""
    with allure.step("Log in"):
        app.header.click_icon()
        app.header.click_log_in()
        app.sign_in_page.enter_sign_in_email(user)
        app.sign_in_page.enter_sign_in_password(password)
        app.sign_in_page.click_sign_in()
    with allure.step('Check if user logined'):
        assert app.header.is_logined(), "No 'log out' link"
        app.header.click_icon()
    with allure.step('Check if user authorized'):
        assert app.header.get_text_of_first_link() == expected, 'Wrong link text'
    with allure.step("Log out"):
        app.header.click_icon()
        app.header.click_log_out()
