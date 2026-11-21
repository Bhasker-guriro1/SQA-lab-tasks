from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/html/html_tables.asp")

    wait = WebDriverWait(driver, 10)

    xpath = "(//table)[1]//tr[3]/td[2]"
    cell = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    print("Located table cell text:", cell.text)

finally:
    driver.quit()
