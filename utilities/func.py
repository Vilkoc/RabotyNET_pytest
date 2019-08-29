"""This module contains login method"""


def login(sign_in_page, user, password):
    """Method for user log in"""
    sign_in_page.enter_sign_in_email(user)
    sign_in_page.enter_sign_in_password(password)
    sign_in_page.click_sign_in()
