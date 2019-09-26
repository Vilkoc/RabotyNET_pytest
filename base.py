import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
URL = 'https://teck-ui-qa-dot-teck-dev-dabs-optimization.appspot.com/login'
driver.maximize_window()
driver.get(URL)

USERNAME = (By.ID, "mat-input-0")
PASSWORD = (By.ID, "mat-input-1")
LOGIN = (By.CSS_SELECTOR, 'span[class="mat-button-wrapper"]')

url = driver.current_url

while url == URL:
    driver.find_element(*USERNAME).send_keys('test@mail.com')
    driver.find_element(*PASSWORD).send_keys('VeryStrongPassword')
    driver.find_element(*LOGIN).click()
    time.sleep(7)
    url = driver.current_url

BRIDGE2 = (By.CSS_SELECTOR, 'button[aria-label="toggle BRIDGE2"]')
L_1575 = (By.CSS_SELECTOR, 'button[aria-label="toggle 1575"]')
L_00 = (By.CSS_SELECTOR, 'button[aria-label="toggle 00"]')
L_02 = (By.CSS_SELECTOR, 'div[class="mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin"]')
POLYGON_TOOL = (By.CSS_SELECTOR, 'button[title="Polygon tool (p)"]')
VISIBILITY_SETTINGS = (By.CSS_SELECTOR, 'button[class="reset-btn visibility-btn"]')

driver.find_element(*BRIDGE2).click()
driver.find_element(*L_1575).click()
driver.find_element(*L_00).click()
driver.find_element(*L_02).click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located(POLYGON_TOOL))
driver.find_element(*POLYGON_TOOL).click()
driver.find_element(*VISIBILITY_SETTINGS).click()




# EVO = (By.XPATH, "//span[ text()='EVO']")
# GHO = (By.XPATH, "//span[ text()='GHO']")
# LCO = (By.XPATH, "//span[ text()='LCO']")

# try:
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located(EVO))
# except TimeoutException:
#     driver.find_element(*USERNAME).clear()
#     driver.find_element(*USERNAME).send_keys('test@mail.com')
#     driver.find_element(*PASSWORD).clear()
#     driver.find_element(*PASSWORD).send_keys('VeryStrongPassword')
#     driver.find_element(*LOGIN).click()
#
#
#
# driver.find_element(*EVO).click()
# time.sleep(1)
# driver.find_element(*LCO).click()
# time.sleep(1)
# driver.find_element(*GHO).click()
# time.sleep(3)

# driver.quit()