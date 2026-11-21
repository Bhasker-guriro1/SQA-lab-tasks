from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.wikipedia.org")
    time.sleep(2)

    links = driver.find_elements(By.TAG_NAME, "a")
    print("Total links found on Wikipedia:", len(links))

finally:
    driver.quit()
