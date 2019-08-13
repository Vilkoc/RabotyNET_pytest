from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage
from pages.my_companies_page import MyCompaniesPage
from pages.update_company_page import UpdateCompanyPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.create_company_page import CreateCompanyPage


class Application():
    """The parent class for all tests"""

    def __init__(self, driver_init):
        self.driver_init = driver_init
        self.header = Header(self.driver_init)
        self.sign_in_page = SignInPage(self.driver_init)
        self.vacancies_page = VacanciesPage(self.driver_init)
        self.view_vacancy_page = ViewVacancyPage(self.driver_init)
        self.preview_resume_page = PreviewResumePage(self.driver_init)
        self.edit_resume_page = EditResumePage(self.driver_init)
        self.view_company_page = ViewCompanyPage(self.driver_init)
        self.companies_page = CompaniesPage(self.driver_init)
        self.my_companies_page = MyCompaniesPage(self.driver_init)
        self.update_company_page = UpdateCompanyPage(self.driver_init)
        self.create_vacancy_page = CreateVacancyPage(self.driver_init)
        self.create_company_page = CreateCompanyPage(self.driver_init)

