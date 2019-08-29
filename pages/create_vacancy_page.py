"""This module contains methods that allow company owner to create a vacancy"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import LocatorsCreateVacancyPage
from locators import LocatorsCreateCompanyPage
from config import TIMEOUT


class CreateVacancyPage():
    """On this page company owner can create vacancy after creation of the company"""

    def __init__(self, browser):
        self.locators = LocatorsCreateVacancyPage
        self.loc = LocatorsCreateCompanyPage
        self.browser = browser
        self.wait = WebDriverWait(browser.driver, TIMEOUT)

    def enter_vacancy_data(self, vac_data):
        """Enters into the specific field data"""
        for field in range(len(self.locators.VACANCY_FIELDS)):
            self.browser.send_keys((By.ID, self.locators.VACANCY_FIELDS[field]), vac_data[field])

    def choose_employment(self):
        """Choosing the employment type from the drop-down list"""
        self.browser.click_element(self.locators.VACANCY_EMPLOYMENT_DROPBOX)

    def choose_currency(self):
        """Choosing the currency from the drop-down list"""
        self.browser.click_element(self.locators.VACANCY_CURRRENCY_DROPBOX)

    def click_add_requirement(self):
        """Clicks on the 'add' button that adds a requirement"""
        self.browser.click_element(self.locators.ADD_REQUIREMENT_BUTTON)

    def enter_requirements(self, req):
        """Enters into the requirement fields data"""
        self.click_add_requirement()
        all_req_fields = self.browser.get_elements(self.locators.VAC_REQUIREMENT_TEXTBOX)
        index_of_textbox = 0
        for req_field in all_req_fields:
            req_field.send_keys(req[index_of_textbox])
            index_of_textbox += 1

    def click_vacancy_create(self):
        """Clacks on the 'Create' vacancy that saves all vacancy data"""
        self.browser.get_element(self.locators.VACANCY_CREATE_BUTTON).click()

    def read_vacancy_data(self):
        """Extracts text data from specified textbox"""
        vacancy_data = self.browser.read_data_in_textbox(self.locators.VACANCY_FIELDS,
                                                         self.loc.ATTRIBUTE_OF_COMPANIES_VACANCIES_TEXTBOXES)
        return vacancy_data
