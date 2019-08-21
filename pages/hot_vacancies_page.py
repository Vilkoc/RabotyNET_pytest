from locators import LocatorsHotVacancies
from data_tests import guest_data


class HotVacanciesPage():
    """On this page users can view details of hot vacancies"""

    def __init__(self, browser):
        self.locators = LocatorsHotVacancies
        self.browser = browser

    def view_details(self):
        self.browser.click_element(self.locators.HOT_DETAILS)
        self.browser.click_element(self.locators.HOT_VACANCY_PAGE)

    def click_pagination_next(self):
        self.browser.click_element(self.locators.HOT_VACANCY_PAGE)
        self.browser.click_element_by_text(self.locators.HOT_PAGINATION_NEXT, guest_data.HOT_NEXT)

    def click_pagination_previous(self):
        self.browser.click_element_by_text(self.locators.HOT_PAGINATION_PREVIOUS, guest_data.HOT_PREVIOUS)

    def details_text(self):
        text_details = self.browser.pop_up_element(self.locators.HOT_VACANCY_INFO).text
        return text_details

    def next_click_test(self):
        click_next = self.browser.pop_up_element(self.locators.HOT_NEXT_TEST).text
        return click_next

    def previous_click_test(self):
        click_previous = self.browser.pop_up_element(self.locators.HOT_PREVIOUS_TEST).text
        return click_previous
