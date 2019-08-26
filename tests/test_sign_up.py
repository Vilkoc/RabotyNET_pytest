""" This module automate testing for sign up new user """
import allure
from data_tests.auth import USERNAME_SIGNUP, PASSWORD, USER_MAIL, WRONG_MAIL, PASSWORD_INCORRECT
from utilities.func import login
from utilities.db import change_varification_link, wait_user_update

MOCK_CONFIRMATION_LINK = 'http://localhost:4200/users/auth/confirm?token=3e83667c-c59c-4fda-aa7a-a47346a3cd6a'


@allure.feature('Sign up')
def test_sign_up(app, make_screen):
    """ Test case for sign up user. """
    app.header.click_icon()
    app.header.click_log_in()

    app.sign_in_page.click_sign_up_tab()

    app.sign_in_page.enter_sign_up_email(USERNAME_SIGNUP)
    app.sign_in_page.enter_sign_up_password(PASSWORD)
    app.sign_in_page.enter_sign_up_matching_password(PASSWORD)
    app.sign_in_page.click_sing_up_button()

    with allure.step('Is confirmation sent on email?'):
        assert app.vacancies_page.is_confirmation_sent(), "No confirmation pop up window"

    change_varification_link(USERNAME_SIGNUP)
    app.vacancies_page.click_confirmation_link(MOCK_CONFIRMATION_LINK)

    wait_user_update(USERNAME_SIGNUP)

    login(app.sign_in_page, USERNAME_SIGNUP, PASSWORD)
    with allure.step('Is user authenticated?'):
        assert app.header.is_logined(), "No 'log out' link"


@allure.feature('Sign up')
@allure.story('Sign up negative')
def test_sign_up_negative_email(app, make_screen):
    """ Test case for sign up user.
    Negative. Using email already registered user"""
    app.header.click_icon()
    app.header.click_log_in()

    app.sign_in_page.click_sign_up_tab()

    app.sign_in_page.enter_sign_up_email(USER_MAIL)
    app.sign_in_page.enter_sign_up_password(PASSWORD)
    app.sign_in_page.enter_sign_up_matching_password(PASSWORD)
    app.sign_in_page.click_sing_up_button()

    with allure.step('Is email already taken?'):
        assert app.vacancies_page.is_email_taken()


@allure.feature('Sign up')
@allure.story('Sign up negative')
def test_sign_up_negative_password(app, make_screen):
    """ Test case for sign up user.
    Negative. Using incorrect password """
    app.header.click_icon()
    app.header.click_log_in()

    app.sign_in_page.click_sign_up_tab()

    app.sign_in_page.enter_sign_up_email(USER_MAIL)
    app.sign_in_page.enter_sign_up_password(PASSWORD_INCORRECT)
    app.sign_in_page.enter_sign_up_matching_password(PASSWORD_INCORRECT)
    app.sign_in_page.click_sing_up_button()

    with allure.step('Is message about wrong password?'):
        assert app.sign_in_page.is_password_sign_up_wrong()


@allure.feature('Sign up')
@allure.story('Sign up negative')
def test_sign_up_negative_email_wrong(app, make_screen):
    """ Test case for sign up user.
    Negative. Using incorrect email """
    app.header.click_icon()
    app.header.click_log_in()

    app.sign_in_page.click_sign_up_tab()

    app.sign_in_page.enter_sign_up_email(WRONG_MAIL)
    app.sign_in_page.enter_sign_up_password(PASSWORD)
    app.sign_in_page.enter_sign_up_matching_password(PASSWORD)
    app.sign_in_page.click_sing_up_button()

    with allure.step('Is message about wrong email?'):
        assert app.sign_in_page.is_email_wrong()


@allure.feature('Sign up')
@allure.story('Sign up negative')
def test_sign_up_negative_password_mismatch(app, make_screen):
    """ Test case for sign up user.
    Negative. Using different password and matching password """
    app.header.click_icon()
    app.header.click_log_in()

    app.sign_in_page.click_sign_up_tab()

    app.sign_in_page.enter_sign_up_email(USER_MAIL)
    app.sign_in_page.enter_sign_up_password(PASSWORD)
    app.sign_in_page.enter_sign_up_matching_password(PASSWORD + 'a')
    app.sign_in_page.click_sing_up_button()

    with allure.step('Is message about different passwords?'):
        assert app.sign_in_page.is_passwords_mismatch()
