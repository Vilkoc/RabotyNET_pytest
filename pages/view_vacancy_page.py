"""This module contains methods that allow user to send resume and look through company info"""
from locators import LocatorsViewVacancy


class ViewVacancyPage():
    """On this page users can return to all vacancies page, view info about company,
    and go to preview resume"""

    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsViewVacancy

    def click_send_resume_button(self):
        """Clicks on the 'Send Resume' button"""
        self.browser.click_element_double_locator(self.locators.TEXT,
                                                  self.locators.SEND_RESUME_BUTTON)

    def click_show_company_button(self):
        """Clicks on the 'Show Company' button"""
        self.browser.click_element(self.locators.SHOW_COMPANY_BUTTON)
