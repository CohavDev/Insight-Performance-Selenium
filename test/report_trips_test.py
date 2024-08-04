from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.pages.loginpage import LoginPage
from src.pages.dashboard import Dashboard
from src.pages.reportpage import ReportPage
from src.tools.timer import Timer
import time

# import json
# json_file_path = "env_config.json"
# with open(json_file_path, "r") as file:
#     env_data = json.load(file)
# config = env_data["QA_IL"]

def test_gen_report_trips(config):
    config["test_case"] = "test_gen_report_trips"
    timer = Timer(config)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    print("--- starting test case ---")
    print(config["user"]["name"])
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.get(config["URL"])

    login_page = LoginPage(driver)
    login_page.select_username(config["user"]["name"])
    login_page.select_password(config["user"]["pass"])
    timer.start()
    login_page.click_signin()
    login_page.wait_for_login()
    timer.end("Logged in Successfully")
    timer.logEvent("Login finished")
    time.sleep(2)

    # Dashboard -> Vehicles
    dashboard = Dashboard(driver)
    reports = ReportPage(driver)
    timer.start()
    dashboard.navigate_reports()
    reports.genereate_trips_report()
    timer.end("genereated report")
    timer.logEvent("Navigation: Reports Tab + trips report")
    time.sleep(10)
    driver.quit()
    print("--- finished test case ---")
