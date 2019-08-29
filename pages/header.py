"""This module contains methods connected with navigation bar"""
from locators import LocatorsHeader
from locators import LocatorsCreateCompanyPage
from locators import LocatorsMyCompaniesPage
from locators import LocatorsYourResume


class Header:
    """This is navigation panel present for all pages"""
<<<<<<< HEAD

=======
>>>>>>> 03e74acc2a367aa8536247c1003d544265edf86a
    def __init__(self, browser):
        self.browser = browser
        self.locators = LocatorsHeader
        self.locator_create_company = LocatorsCreateCompanyPage
        self.locator_my_companies = LocatorsMyCompaniesPage
        self.locators_your_resume = LocatorsYourResume

    def click_icon(self):
        """Clicks on the round icon"""
        self.browser.click_element(self.locators.ICON)

    def check_dropdown(self):
        """Verifies if the dropdown box appeared"""
        flag = self.browser.get_attr_value(self.locators.CHECK_DROPDOWN, 'aria-expanded')
        return True if flag == 'true' else False

    def click_log_out(self):
        """Clicks on the round icon"""
        self.browser.click_element_by_text(self.locators.LOG_OUT, "Log out")

    def click_log_in(self):
        """Clicks on the round icon"""
        self.browser.wait_element_with_text(self.locators.LOG_IN, "Log in")
        self.browser.click_element_by_text(self.locators.LOG_IN, "Log in")

    def is_logined(self):
        """ Check if user logined: if 'logout' button exist == logined """
        self.click_icon()
        log_out = self.browser.wait_element_with_text(self.locators.LOG_OUT, "Log out")
        return log_out.text == 'Log out'

    def select_option(self, pick_item):
        """The pick_item is default string parameter which accepts only 'Log in',
        'Profile', 'Log out' values"""
        values = ('Log in', 'Profile', 'Log out')
        if pick_item not in values:
            raise Exception('Incorrect value for click_dropdown function')
        self.click_icon()
<<<<<<< HEAD
        if pick_item == 'Profile':
            while self.check_dropdown():
                self.browser.click_element_by_text(self.locators.DROPDOWN, pick_item)
            else:
                self.click_icon()
        else:
            if self.check_dropdown():
                self.browser.click_element_by_text(self.locators.DROPDOWN, pick_item)
            else:
                self.click_icon()
=======
        while self.check_dropdown():
            self.browser.click_element_by_text(self.locators.DROPDOWN, pick_item)
        else:
            self.click_icon()
>>>>>>> 03e74acc2a367aa8536247c1003d544265edf86a

    def person_verify(self, person):
        """Returns True if the number of elements on the navbar equals to the person_criteria"""
        person_criteria = {'ADMIN': 3, 'USER': 4, 'COWNER': 6}
        current_person = 2
        while current_person < person_criteria[person]:
            current_person = len(self.browser.get_elements(self.locators.NAVBAR))
        return True if current_person == person_criteria[person] else False

    def move_to_companies(self):
        """Clicks on 'Companies' button"""
        self.browser.click_element(self.locators.MOVE_TO_COMPANIES)

    def click_create_company(self):
        """Clicks on 'Create company' button"""
        self.browser.click_element(self.locator_create_company.CREATE_COMPANY_TAB)

    def click_my_companies(self):
        """Clicks on 'My Companies' button"""
        self.browser.click_element(self.locator_my_companies.MY_COMPANIES)

    def get_text_of_first_link(self):
        """Returns the text of the first link in the header"""
        self.browser.wait_of_quantity_elements(self.locators.LINKS, 3)
        return self.browser.get_elements(self.locators.LINKS)[1].text

    def go_to_all_vacancies(self):
        """Clicks on the 'RabotyNEY' button in the header"""
        self.browser.click_element_double_locator(self.locators_your_resume.SHOW_ALL_INFO_BUTTON,
                                                  self.locators.RABOTY_NET)
