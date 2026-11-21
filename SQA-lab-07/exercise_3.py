
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")
print(driver.title)
time.sleep(5)

driver.get("https://youtube.com")
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)

driver.forward()
print(driver.title)
time.sleep(5)

driver.switch_to.new_window("tab")
driver.get("https://wikipedia.org")
print(driver.title)
time.sleep(5)

driver.close()
time.sleep(2)

driver.quit()

