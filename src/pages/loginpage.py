from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        
    locators = {
        'user_name' : ('CSS', 'div[system_id="543932_control_container_panel"] input'),
        'password' : ('CSS', 'div[system_id="543929_control_container_panel"] input'),
        'button': ('CSS','div[system_id="543914"]'),
        'bell_icon':('CSS', 'div[system_id="482336_control_container_panel"]')

    }
    def select_username(self, user):
        self.user_name.set_text(user)

    def select_password(self, password):
        self.password.set_text(password)

    def click_signin(self):
        self.button.click()

    def wait_for_login(self):
        wait = WebDriverWait(self.driver, timeout=30)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['bell_icon'][1] )))
        print("--> Logged in successfully")
