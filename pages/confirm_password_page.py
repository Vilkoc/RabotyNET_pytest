"""This module contains methods that helps user to change his/her password"""
from locators import LocatorsConfirmPassword


class ConfirmPassword:
    """Confirm new password"""

    def __init__(self, base_obj):
        self.browser = base_obj
        self.locators = LocatorsConfirmPassword

    def enter_new_password(self, password):
        """Enters into the password field a new password"""
        self.browser.send_keys(self.locators.NEW_PASSWORD, password)

    def enter_confirm_password(self, password):
        """Enters into the password field a new password for confirmation"""
        self.browser.send_keys(self.locators.CONFIRMATION_PASSWORD, password)

    def click_register_button(self):
        """Clicks on the 'Register' button"""
        self.browser.click_element(self.locators.REGISTER_BUTTON)
