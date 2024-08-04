from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


class ReportPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        
    locators = {
        'fleet_util':('CSS','div[system_id="544111"]'),
        'fleet_util_items':('CSS','div[system_id="544129"]'),

        'vehicle_detailed_trips':('CSS','div[system_id="544124"]'),
        'date_selection':('CSS','div[system_id="544254"]'),
        'start_date_btn':('CSS','div[system_id="565543"] div.date_time_calendar_button'),
        'end_date_btn':('CSS', 'div[system_id="565546"] div.date_time_calendar_button'),
        'apply_date_btn':('CSS','div[system_id="565541"]'),
        'vehicles_selection':('CSS','div[system_id="544308"]'),
        'first_row':('CSS','div[system_id="565307"]'),
        'select_all_checkbox':('CSS','div[system_id="checkbox_cell0_control_container_panel"]'),
        'apply_vehicles_btn':('CSS','div[system_id="565295"]'),
        'gen_report_btn':('CSS','div[system_id="554269"]'),
        'loading_icon':('CSS','div[system_id="471677"]')
        

    }
    def genereate_trips_report(self):
        print("waiting for report side menu")
        wait = WebDriverWait(self.driver, timeout=60)
        elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.locators['fleet_util'][1] )))
        print("clicking fleet util")
        elements[1].click()
        time.sleep(1)
        elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, self.locators['vehicle_detailed_trips'][1] )))
        wait.until(EC.element_to_be_clickable(elements[0]))
        print("click trips")
        elements[0].click()
        print("clicked!")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['date_selection'][1] )))
        print("click date selection")
        self.date_selection.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['start_date_btn'][1] )))
        # choose current day at 00:00
        self.start_date_btn.click()
        self.start_date_btn.click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['end_date_btn'][1] )))
        # choose current day at 23:59
        self.end_date_btn.click()
        self.end_date_btn.click()
        print("click apply date")
        self.apply_date_btn.click()
        print("clicked")
        # choose vehicles
        self.driver.find_elements(By.CSS_SELECTOR,self.locators['vehicles_selection'][1])[1].click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators['first_row'][1] )))
        self.select_all_checkbox.click()
        self.apply_vehicles_btn.click()
        self.gen_report_btn.click()
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, self.locators['loading_icon'][1] )))
        print("generated report!")
        # time.sleep(20)






