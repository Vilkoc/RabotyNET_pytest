"""This module contains method that choose needed browser"""
from selenium import webdriver


class WebdriverSelection():
    """Select a browser"""
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name.lower() == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")

            return webdriver.Chrome()

        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser_name.lower() == 'opera':
            return webdriver.Opera()
        else:
            raise Exception("There's no available driver for such browser")
