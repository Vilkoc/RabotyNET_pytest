from locators import LocatorsCreateCompanyPage, LocatorsMyCompaniesPage, LocatorsVacancies
from selenium.webdriver.common.by import By


class CreateCompanyPage():
    """On this page company owner can create his/her own company by filling input fields with needed
    data snd click create"""

    def __init__(self, browser):
        self.locators = LocatorsCreateCompanyPage
        self.locators_my_companies = LocatorsMyCompaniesPage
        self.locators_vacancies = LocatorsVacancies
        self.browser = browser

    def enter_data(self, co_data):
        """Enters into the specific field data"""
        for el in range(len(self.locators.COMPANY_FIELDS)):
            self.browser.send_keys((By.ID, self.locators.COMPANY_FIELDS[el]), co_data[el])

    def click_create_button(self):
        self.browser.click_element(self.locators.COMPANY_CREATE_BUTTON)

    def click_my_companies_tab(self):
        self.browser.click_element_double_locator(self.locators_vacancies.DETAILS, self.locators_my_companies.MY_COMPANIES)

    def read_data(self):
        input_data = self.browser.read_data_in_textbox(self.locators.COMPANY_FIELDS,
                                                       self.locators.ATTRIBUTE_OF_COMPANIES_VACANCIES_TEXTBOXES)
        return input_data
