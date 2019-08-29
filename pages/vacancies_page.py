"""This module contains methods that allow company owner and user to lock through
vacancies details"""
from locators import LocatorsVacancies
from data_tests import guest_data


class VacanciesPage:
    """On this page user or company owner can view vacancies"""

    def __init__(self, base_obj):
        self.browser = base_obj
        self.locators = LocatorsVacancies

    def is_confirmation_sent(self):
        """Returns True if text from the pop-up window after sending a confirmation is the same
        as a specific one"""
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_SIGN_UP_TEXT)
        return text == 'User has been created successfully. Confirm your email and login into site!'

    def click_confirmation_link(self, link):
        """Clicks on the confirmation link"""
        self.browser.driver.get(link)

    def is_instructions_sent(self):
        """Returns True if text from the pop-up window after link confirmation is the same
        as specific one"""
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_TEXT)
        return text == 'Please check mail for further instructions!'

    def is_email_taken(self):
        """Returns the True if the text from the pop-up window is the same as specific one"""
        text = self.browser.get_text_of_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_TEXT)
        return text == 'There is an account with that email! Try with another one or login, please!'

    def click_ok(self):
        """Clicks on the 'Ok' button"""
        self.browser.click_element(self.locators.POP_UP_WINDOW_FORGOT_PASSWORD_BUTTON)

    def click_view_details_button(self):
        """Clicks on the 'View details' button"""
        self.browser.click_element(self.locators.VIEW_DETAILS_BUTTON)

    def view_details(self):
        """Shows all the vacancies on the main page"""
        self.browser.click_element(self.locators.DETAILS)
        self.browser.click_element(self.locators.RABOTY_NET)

    def click_pagination_next(self):
        """Clicks on the 'Next' button"""
        self.browser.click_element_by_text(self.locators.PAGINATION_NEXT, guest_data.NEXT)

    def click_pagination_previous(self):
        """Clicks on the 'Previous' button"""
        self.browser.click_element_by_text(self.locators.PAGINATION_PREVIOUS, guest_data.PREVIOUS)

    def details_text(self):
        """Returns the detailed vacancy information"""
        text_details = self.browser.pop_up_element(self.locators.VACANCY_INFO).text
        return text_details

    def next_click_test(self):
        """Returns the vacancy data after clicking on the 'Next' button"""
        click_next = self.browser.pop_up_element(self.locators.NEXT_TEST).text
        return click_next

    def previous_click_test(self):
        """Returns the vacancy data after clicking on the 'Previous' button"""
        click_previous = self.browser.pop_up_element(self.locators.PREVIOUS_TEST).text
        return click_previous
