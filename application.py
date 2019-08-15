from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage


class Application():
    """The parent class for all tests"""

    def __init__(self, browser_init):
        self.browser_init = browser_init
        self.header = Header(self.browser_init)
        self.sign_in_page = SignInPage(self.browser_init)
        self.vacancies_page = VacanciesPage(self.browser_init)
        self.view_vacancy_page = ViewVacancyPage(self.browser_init)
        self.preview_resume_page = PreviewResumePage(self.browser_init)
        self.edit_resume_page = EditResumePage(self.browser_init)
        self.view_company_page = ViewCompanyPage(self.browser_init)
        self.companies_page = CompaniesPage(self.browser_init)
