from selenium import webdriver
from src.pages.loginpage import LoginPage
from src.pages.dashboard import Dashboard
from src.pages.mapview import MapView
from src.tools.timer import Timer
import time
import json

json_file_path = "env_config.json"
with open(json_file_path, "r") as file:
    env_data = json.load(file)

config = env_data["QA_IL"]
def test_maps():
    timer = Timer()
    print("--- starting test case ---")
    print(config["user"]["name"])
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.get(config["URL"])

    timer.start()
    login_page = LoginPage(driver)
    login_page.select_username(config["user"]["name"])
    login_page.select_password(config["user"]["pass"])
    login_page.click_signin()
    login_page.wait_for_login()
    timer.end("Logged in Successfully")
    time.sleep(2)

    # Dashboard -> Map View
    dashboard = Dashboard(driver)
    mapview = MapView(driver)
    timer.start()
    dashboard.navigate_mapview()
    mapview.wait_tableloaded()
    timer.end("Navigated to map view")
    time.sleep(120)
    driver.quit()
    print("--- finished test case ---")

try:
    test_maps()
except Exception as e:
    print("\nAn error occured: ",e)