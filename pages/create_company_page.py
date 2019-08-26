"""This module contains methods that allow company owner to create a company"""
from selenium.webdriver.common.by import By
from locators import LocatorsCreateCompanyPage, LocatorsMyCompaniesPage, LocatorsVacancies


class CreateCompanyPage():
    """On this page company owner can create his/her own company by filling input fields with needed
    data snd click create"""

    def __init__(self, browser):
        self.locators = LocatorsCreateCompanyPage
        self.locators_my_companies = LocatorsMyCompaniesPage
        self.locators_vacancies = LocatorsVacancies
        self.browser = browser

    def enter_data(self, co_data):
        """Enters into the specific fields data"""
        for field in range(len(self.locators.COMPANY_FIELDS)):
            self.browser.send_keys((By.ID, self.locators.COMPANY_FIELDS[field]), co_data[field])

    def click_create_button(self):
        """Clicks on the 'Create' button"""
        self.browser.click_element(self.locators.COMPANY_CREATE_BUTTON)

    def click_my_companies_tab(self):
        """Clicks on the 'all companies' item"""
        self.browser.click_element_double_locator(self.locators_vacancies.DETAILS,
                                                  self.locators_my_companies.MY_COMPANIES)

    def read_data(self):
        """Extracts text data from specified textbox"""
        input_data = self.browser.read_data_in_textbox(self.locators.COMPANY_FIELDS,
                                                       self.locators.ATTRIBUTE_OF_COMPANIES_VACANCIES_TEXTBOXES)
        return input_data
