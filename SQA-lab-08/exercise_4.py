from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/login")

    wait = WebDriverWait(driver, 10)

    by_id = wait.until(EC.presence_of_element_located((By.ID, "username")))
    print("Username field found using ID.")

    by_name = driver.find_element(By.NAME, "username")
    print("Username field found using NAME.")

    by_css = driver.find_element(By.CSS_SELECTOR, "input#username")
    print("Username field found using CSS SELECTOR.")

finally:
    driver.quit()
