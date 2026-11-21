from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()

    # Open the first website.
    driver.get("https://www.google.com")
    time.sleep(2)
    print("First website title:", driver.title)
    print("First website URL:", driver.current_url)

    # Navigate to the second website.
    driver.get("https://www.wikipedia.org")
    time.sleep(2)
    print("Second website title:", driver.title)
    print("Second website URL:", driver.current_url)

    # Go back to the first website.
    driver.back()
    time.sleep(2)
    print("After Back:", driver.title)

    # Go forward to the second website.
    driver.forward()
    time.sleep(2)
    print("After Forward:", driver.title)

    # Refresh the current page.
    driver.refresh()
    time.sleep(2)
    print("After Refresh:", driver.title)

finally:
    driver.quit()
