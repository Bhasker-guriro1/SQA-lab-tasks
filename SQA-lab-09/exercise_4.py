from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    wait = WebDriverWait(driver, 10)

    checkboxes = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='checkbox']"))
    )
    checkbox = checkboxes[0]

    initial_state = checkbox.is_selected()
    print("Initial checkbox state:", initial_state)

    checkbox.click()
    after_first_click = checkbox.is_selected()
    print("State after first click:", after_first_click)

    checkbox.click()
    after_second_click = checkbox.is_selected()
    print("State after second click:", after_second_click)

    print("Returned to initial state:", initial_state == after_second_click)

finally:
    driver.quit()
