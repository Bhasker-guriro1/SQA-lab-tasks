from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://demoqa.com/radio-button")
    wait = WebDriverWait(driver, 10)

    # Select Yes, then verify the selected state.
    yes_label = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='yesRadio']"))
    )
    yes_label.click()
    yes_radio = driver.find_element(By.ID, "yesRadio")
    print("Yes selected:", yes_radio.is_selected())

    # Select Impressive. Radio buttons in the same group are mutually exclusive.
    impressive_label = driver.find_element(
        By.CSS_SELECTOR, "label[for='impressiveRadio']"
    )
    impressive_label.click()

    impressive_radio = driver.find_element(By.ID, "impressiveRadio")
    print("Impressive selected:", impressive_radio.is_selected())
    print("Yes selected after choosing Impressive:", yes_radio.is_selected())

finally:
    driver.quit()
