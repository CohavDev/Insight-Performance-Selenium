from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait
class Dashboard(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,30)
        
    locators = {
        'dashboard_maintenance':('CSS','div[system_id="565832"]'),
        'dashboard_diagnostics':('CSS','div[system_id="565833"]'),
        'dashboard_predictions':('CSS','div[system_id="565834"]'),
        'dashboard_ams':('CSS','div[system_id="565835"]'),
        'dashboard_software_updates':('CSS','div[system_id="716252"]'),
        #
        'mapview' : ('CSS', 'div[system_id="481870_control_container_panel"]'),
        'reports':('CSS','div[system_id="544095_control_container_panel"]'),
        'vehicles':('CSS','div[system_id="481872_control_container_panel"]'),
        'drivers':('CSS', 'div[system_id="531442_control_container_panel"]'), 
    }
    def navigate_dashboard_maintenance(self):
        self.dashboard_maintenance.click()

    def navigate_dashboard_diagnostics(self):
        self.dashboard_diagnostics.click()

    def navigate_dashboard_predictions(self):
        self.dashboard_predictions.click()

    def navigate_dashboard_ams(self):
        self.dashboard_ams.click()

    def navigate_dashboard_software_updates(self):
        self.dashboard_software_updates.click()

    def navigate_mapview(self):
        print("--> loading mapview vehicles")
        self.mapview.click()

    def navigate_reports(self):
        self.reports.click()

    def navigate_vehicles(self):
        self.vehicles.click()

    def navigate_drivers(self):
        self.drivers.click()
    