from selenium import webdriver
from src.pages.loginpage import LoginPage
from src.pages.dashboard import Dashboard
from src.pages.mapview import MapView
from src.tools.timer import Timer
import time

def test_maps(config):
    timer = Timer(config)
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
    timer.logEvent("Login finished")

    time.sleep(2)

    # Dashboard -> Map View
    dashboard = Dashboard(driver)
    mapview = MapView(driver)
    timer.start()
    dashboard.navigate_mapview()
    mapview.wait_tableloaded()
    timer.end("Navigated to map view")
    timer.logEvent("Navigation: Map Tab")
    time.sleep(120)
    driver.quit()
    print("--- finished test case ---")
