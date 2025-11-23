# Python Configuration file for End-to-End Testing of Homepage
# Description: This file is configured with pytest to run Selenium tests on the homepage.
# This script tests the homepage of a webpage by navigating to the "About Us" page and then returning to the homepage by clicking the logo.
# It uses pytest and Selenium WebDriver with Chrome in headless mode. 
# The test sets the browser window size to 1094x943 pixels and is intended to be run in an end-to-end testing environment.


# tests/e2e/test_homepage.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "http://us-east-1-jdevops-webpage.s3-website-us-east-1.amazonaws.com"

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1094, 943)
    yield driver
    driver.quit()

def test_home_page_live(driver):
    driver.get(BASE_URL)
    # Click botton "Read More"
    driver.find_element(By.LINK_TEXT, "Read More").click()
    clicked = True
    # Click botton "Let's Talk"
    driver.find_element(By.LINK_TEXT, "Let's Talk").click()
    clicked = True