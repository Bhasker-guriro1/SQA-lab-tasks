from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/html/html_forms.asp")
    time.sleep(2)

    text_inputs = driver.find_elements(
        By.CSS_SELECTOR, "input[type='text']"
    )

    print("Number of text input elements:", len(text_inputs))

    for index, element in enumerate(text_inputs, start=1):
        element_id = element.get_attribute("id")
        element_name = element.get_attribute("name")
        placeholder = element.get_attribute("placeholder")

        print(
            f"Input {index}: "
            f"id={element_id!r}, "
            f"name={element_name!r}, "
            f"placeholder={placeholder!r}"
        )

finally:
    driver.quit()
