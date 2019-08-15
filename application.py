from pages.header import Header
from pages.sign_in_page import SignInPage
from pages.user_profile_page import UserPage


class SeleniumTestBase():
    """The parent class for all tests"""

    def __init__(self, driver_init):
        self.driver_init = driver_init
        self.header = Header(self.driver_init)
        self.sign_in_page = SignInPage(self.driver_init)
        self.user_profile_page = UserPage(self.driver_init)

