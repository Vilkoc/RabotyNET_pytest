from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.confirm_password_page import ConfirmPassword
from pages.vacancies_page import VacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage


class Application():
    """The parent class for all tests"""

    def __init__(self, driver_init):
        self.driver_init = driver_init
        self.header = Header(self.driver_init)
        self.sign_in_page = SignInPage(self.driver_init)
        self.forgot_password_page = ForgotPasswordPage(self.driver_init)
        self.confirmation_password_page = ConfirmPassword(self.driver_init)
        self.vacancies_page = VacanciesPage(self.driver_init)
        self.view_vacancy_page = ViewVacancyPage(self.driver_init)
        self.preview_resume_page = PreviewResumePage(self.driver_init)
        self.edit_resume_page = EditResumePage(self.driver_init)
        self.view_company_page = ViewCompanyPage(self.driver_init)
        self.companies_page = CompaniesPage(self.driver_init)
