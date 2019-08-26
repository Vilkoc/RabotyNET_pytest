"""This module contains methods that describe the page with company details and allow
the administrator to interaction with it"""
from locators import LocatorsViewCompany


class CompanyDetailsPage():
    """Page with details about company and interaction with it"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsViewCompany

    def create_claim(self):
        """Clicks on the button that creates the claim"""
        self.browser.click_element(self.locators.CLAIM_BUTTON)

    def send_claim(self):
        """Clicks on the button that sends a claim"""
        self.browser.click_element(self.locators.SEND_CLAIM_BUTTON)

    def select_title_of_claim(self):
        """Selects the title of claim from drop-down list"""
        self.browser.click_element(self.locators.TITLE)

    def set_description_of_claim(self):
        """Enters description of a claim"""
        self.browser.send_keys(self.locators.DESCRIPTION_FIELD, self.locators.DESCRIPTION_OF_CLAIM)
