""" This module automate recover password for registered user """
import allure
from config import USERNAME_PASSW_RECOVERY, OLD_PASSWORD, NEW_PASSWORD
from utilities.func import login
from utilities.db import change_varification_link

MOCK_CONFIRMATION_LINK = \
    'http://localhost:4200/confirmPassword?token=3e83667c-c59c-4fda-aa7a-a47346a3cd6a'


@allure.feature('Forgot password')
def test_forgot_password(app, make_screen):
    """ Test case to renew password using email"""
    with allure.step("Login"):
        app.header.click_icon()
        app.header.click_log_in()
    with allure.step("Password renew"):
        app.sign_in_page.click_forgot_password()
        app.forgot_password_page.enter_login_email(USERNAME_PASSW_RECOVERY)
        app.forgot_password_page.click_submit_button()
    with allure.step('Is instruction sent on email?'):
        assert app.vacancies_page.is_instructions_sent()
        app.vacancies_page.click_ok()
        change_varification_link(USERNAME_PASSW_RECOVERY)
        app.vacancies_page.click_confirmation_link(MOCK_CONFIRMATION_LINK)
    with allure.step("Entering a new password"):
        app.confirmation_password_page.enter_new_password(NEW_PASSWORD)
        app.confirmation_password_page.enter_confirm_password(NEW_PASSWORD)
        app.confirmation_password_page.click_register_button()
    with allure.step('Pop up window messaging "password restore"'):
        assert app.sign_in_page.is_password_restored()
        app.sign_in_page.click_ok()

    login(app.sign_in_page, USERNAME_PASSW_RECOVERY, OLD_PASSWORD)
    with allure.step('Is user authenticated?'):
        assert app.header.is_logined()
