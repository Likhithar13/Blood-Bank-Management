from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the Django server before running this script.
# Install a compatible Chrome/Edge browser. Selenium Manager may obtain a driver.
driver = webdriver.Chrome()
try:
    driver.get("http://127.0.0.1:8000/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Dashboard" in driver.page_source
    print("PASS: Dashboard loaded")
finally:
    driver.quit()
