"""This module contains methods that help users to manage resume information"""
from locators import LocatorsPreviewResume


class PreviewResumePage():
    """On this page user or cowner can change information in resume, send resume,
    and open resume in new tab"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsPreviewResume

    def click_send_email_button(self):
        """Clicks on the 'Send Email' button"""
        self.browser.click_element_by_text(self.locators.BUTTONS, 'Send Email')

    def click_change_button(self):
        """Clicks on the 'Change' data"""
        self.browser.click_button_change(self.locators.BUTTONS, self.locators.RESUME)

    def confirmation_message(self):
        """Returns the text from the pop-up message"""
        self.browser.driver.execute_script("window.scrollTo(0, 0);")
        message = self.browser.pop_up_element(self.locators.MESSAGE).text
        return message
