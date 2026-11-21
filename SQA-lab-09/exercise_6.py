from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import Select 
 
driver = webdriver.Chrome() 
 
try: 
    driver.get("https://www.w3schools.com/howto/howto_custom_select.asp") 
 
    # Use a page with a standard HTML <select> element. 
    driver.get("https://www.selenium.dev/selenium/web/formPage.html") 
    wait = WebDriverWait(driver, 10) 
 
    dropdown_element = wait.until( 
        EC.presence_of_element_located((By.NAME, "selectomatic")) 
    ) 
    dropdown = Select(dropdown_element) 
 
    # Select by visible text. 
    dropdown.select_by_visible_text("Four") 
    print("After visible text:", dropdown.first_selected_option.text) 
 
    # Select by index (indexes start at 0). 
    dropdown.select_by_index(2) 
    print("After index 2:", dropdown.first_selected_option.text) 
 
    # Select by value attribute. 
    dropdown.select_by_value("two") 
    print("After value 'two':", dropdown.first_selected_option.text) 
 
finally: 
    driver.quit() 
