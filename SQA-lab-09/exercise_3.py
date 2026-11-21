from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name.send_keys("Ali")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Khan")

    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("ali.khan@example.com")

    # Select the Male gender option using its associated label.
    male_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    male_label.click()

    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("03001234567")

    # Verify entered values.
    print("First name:", first_name.get_attribute("value"))
    print("Last name:", last_name.get_attribute("value"))
    print("Email:", email.get_attribute("value"))
    print("Gender selected:", driver.find_element(By.ID, "gender-radio-1").is_selected())
    print("Mobile:", mobile.get_attribute("value"))

finally:
    driver.quit()
