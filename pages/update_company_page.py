"""This module contains methods that allow company owner to update a company name"""
from locators import LocatorsUpdateCompanyPage
from pages.create_company_page import CreateCompanyPage


class UpdateCompanyPage(CreateCompanyPage):
    """On this page company owner can update company information and save it"""

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = LocatorsUpdateCompanyPage
        self.browser = browser

    def update_company_name(self, company_name):
        """Clears and enters into the 'Name' input field data"""
        self.browser.clear_element(LocatorsUpdateCompanyPage.COMPANY_NAME_TEXBOX)
        self.browser.send_keys(LocatorsUpdateCompanyPage.COMPANY_NAME_TEXBOX, company_name)

    def click_update_company_button(self):
        """Clicks on the 'Update' button"""
        self.browser.click_element(LocatorsUpdateCompanyPage.UPDATE_COMPANY_BUTTON)

    def check_company_name(self):
        """Returns an updated company name"""
        return self.browser.get_attr_value(self.locators.COMPANY_NAME_TEXBOX, "ng-reflect-model")
