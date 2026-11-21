from selenium import webdriver
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    time.sleep(2)

    driver.get("https://www.wikipedia.org")
    time.sleep(2)

    driver.get("https://www.python.org")
    time.sleep(2)

    # Go back twice: Python.org -> Wikipedia -> Google.
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    print("Title after Back twice:", driver.title)

    # Go forward once: Google -> Wikipedia.
    driver.forward()
    time.sleep(2)
    print("Title after Forward once:", driver.title)

finally:
    driver.quit()
