from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.python.org")
    time.sleep(2)

    title_before_refresh = driver.title
    print("Title before refresh:", title_before_refresh)

    driver.refresh()
    time.sleep(2)

    title_after_refresh = driver.title
    print("Title after refresh:", title_after_refresh)

    if title_before_refresh == title_after_refresh:
        print("Result: The page title remained the same after refresh.")
    else:
        print("Result: The page title changed after refresh.")

finally:
    driver.quit()
