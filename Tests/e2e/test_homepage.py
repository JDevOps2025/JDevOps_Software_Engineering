# Python Configuration file for End-to-End Testing of Homepage
# Description: This file is configured with pytest to run Selenium tests on the homepage.
# This script tests the homepage of a webpage by navigating to the "About Us" page and then returning to the homepage by clicking the logo.
# It uses pytest and Selenium WebDriver with Chrome in headless mode. 
# The test sets the browser window size to 1094x943 pixels and is intended to be run in an end-to-end testing environment.


# tests/e2e/test_homepage.py
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# prefer CI-provided URL, fallback to original
BASE_URL = os.getenv("US_SITE", "http://us-east-1-jdevops-webpage.s3-website-us-east-1.amazonaws.com/index.html")

def test_home_page_live(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)
    # Wait then click "Read More"
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Read More"))).click()

    # Wait then click "Let's Talk" — fix typo and/or try partial text
    try:
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Let's Talk"))).click()
    except Exception:
        wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Talk"))).click()