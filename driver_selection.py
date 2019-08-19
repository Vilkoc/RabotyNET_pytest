from selenium import webdriver


class WebdriverSelection():
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome()
        if browser_name.lower() == 'chrome_inc':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument("headless")
            return webdriver.Chrome(chrome_options=chrome_options)
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser_name.lower() == 'opera':
            return webdriver.Opera()
        else:
            raise Exception("There's no available driver for such browser")
