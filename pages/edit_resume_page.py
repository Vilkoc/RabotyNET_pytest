"""This module contains methods that allow user to edit resume"""
from locators import LocatorsEditResume


class EditResumePage():
    """On this page user or cowner can change information in resume"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsEditResume

    def change_position_field(self, position):
        """Updates the data in the position field"""
        self.browser.clear_element(self.locators.POSITION_FIELD)
        self.browser.send_keys(self.locators.POSITION_FIELD, position)

    def click_preview_pdf_button(self):
        """Clicks on the button that allows user to preview resume in PDF format"""
        self.browser.click_element(self.locators.PREVIEW_PDF_BUTTON)

    def confirmation_changes(self):
        """Returns text from the updated field"""
        self.browser.driver.execute_script("window.scrollTo(0, 0);")
        text = self.browser.get_attr_value(self.locators.POSITION_FIELD,
                                           self.locators.GET_TEXT_FROM_FIELD)
        return text
