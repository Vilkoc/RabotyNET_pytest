"""This module initialize project pages"""
from pages.confirm_password_page import ConfirmPassword
from pages.forgot_password_page import ForgotPasswordPage
from pages.company_details_page import CompanyDetailsPage
from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage
from pages.vacancies_page import VacanciesPage
from pages.hot_vacancies_page import HotVacanciesPage
from pages.view_vacancy_page import ViewVacancyPage
from pages.preview_resume_page import PreviewResumePage
from pages.edit_resume_page import EditResumePage
from pages.view_company_page import ViewCompanyPage
from pages.companies_page import CompaniesPage
from pages.search_page import SearchPage
from pages.my_companies_page import MyCompaniesPage
from pages.update_company_page import UpdateCompanyPage
from pages.create_vacancy_page import CreateVacancyPage
from pages.create_company_page import CreateCompanyPage


class Application():
    """The parent class for all tests"""

    def __init__(self, browser_init):
        self.browser_init = browser_init
        self.header = Header(self.browser_init)
        self.sign_in_page = SignInPage(self.browser_init)
        self.forgot_password_page = ForgotPasswordPage(self.browser_init)
        self.confirmation_password_page = ConfirmPassword(self.browser_init)
        self.vacancies_page = VacanciesPage(self.browser_init)
        self.view_vacancy_page = ViewVacancyPage(self.browser_init)
        self.preview_resume_page = PreviewResumePage(self.browser_init)
        self.edit_resume_page = EditResumePage(self.browser_init)
        self.view_company_page = ViewCompanyPage(self.browser_init)
        self.companies_page = CompaniesPage(self.browser_init)
        self.my_companies_page = MyCompaniesPage(self.browser_init)
        self.update_company_page = UpdateCompanyPage(self.browser_init)
        self.create_vacancy_page = CreateVacancyPage(self.browser_init)
        self.create_company_page = CreateCompanyPage(self.browser_init)
        self.company_details_page = CompanyDetailsPage(self.browser_init)
        self.hot_vacancies_page = HotVacanciesPage(self.browser_init)
        self.search_page = SearchPage(self.browser_init)
        self.user_profile_page = UserPage(self.browser_init)
