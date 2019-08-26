"""This module contains methods that describe the page of all companies and allow
the administrator to manage them"""
from locators import LocatorsCompaniesPage


class CompaniesPage():
    """On this page admin can moderate companies"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsCompaniesPage

    def view_detail_about_co(self):
        """Clicks on the 'view details' button near the specific company"""
        self.browser.click_element(self.locators.DETAILS_ABOUT_CO)

    def view_status_of_co(self):
        """Returns True if the specific company has been approved by admin"""
        company_status = self.browser.get_attr_value(self.locators.STATUS_APPROVED, 'title')
        return company_status == 'This company is approved'

    def view_warning_status_of_co(self):
        """Returns True if the specific company has a claim"""
        company_status = self.browser.get_attr_value(self.locators.STATUS_WARNING, 'title')
        return company_status == 'This company has claims'

    def block_co(self):
        """Clicks on the element that blocks the company"""
        self.browser.click_element(self.locators.BLOCK_1_CO)

    def unblock_co(self):
        """Clicks on the element that unblocks the company"""
        self.browser.click_element(self.locators.UNBLOCK_2_CO)

    def approve_co(self):
        """Clicks on the element that approves the company"""
        self.browser.click_element(self.locators.APPROVE_CO)

    def reject_claim(self):
        """Clicks on the button that rejects claims"""
        self.browser.click_element(self.locators.REJECT_CLAIM_BTN)

    def confirm_with_popup(self):
        """Returns the text from the pop-up message"""
        popup = self.browser.driver.get_element(self.locators.POPUP)
        confirm_popup = popup.find_element_by_tag_name('p').text
        return confirm_popup

    def companies_are_visible(self):
        """Checks the existence of companies"""
        companies = self.browser.get_element_with_time_delay(self.locators.TABLE_BODY)
        if companies != 0:
            return True
        return False

    def click_show_claims_button(self):
        """Clicks on the button that shows the claim"""
        self.browser.driver.execute_script("window.scrollTo(0, 0);")
        self.browser.click_element(self.locators.SHOW_CLAIMS_BUTTON)

    def find_description(self, des):
        """Returns company description"""
        elements = self.browser.get_elements(self.locators.DESCRIPTION)
        description = None
        for element in elements:
            if element.text == des:
                description = element.text
        return description
