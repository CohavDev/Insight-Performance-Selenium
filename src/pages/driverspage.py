from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



class DriversPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        
    locators = {
        'first_row':('CSS','div[system_id="587343"]')
    }
    def wait_tableloaded(self):
        print("waiting for drivers")
        wait = WebDriverWait(self.driver, timeout=60)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['first_row'][1] )))
        # print("element in dom!")
        wait.until(lambda d: self.first_row.is_displayed())
        print("--> drivers page loaded")

