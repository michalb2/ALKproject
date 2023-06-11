from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Opening the website: https://www.demoblaze.com/index.html
driver.get("https://www.demoblaze.com/index.html#")

# 2. Choosing the category: Phones
category_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
category_link.click()

# 3. Clicking on the selected phone : Samsung galaxy s6
phone_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")))
phone_name = phone_item.text
phone_item.click()

# 4. Verifying if the price and product description are displayed
phone_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "price-container"))).text
phone_description = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "more-information"))).text

if phone_price and phone_description:
    print(f"Price and product description for {phone_name} are displayed.")
else:
    print(f"Price and product description for {phone_name} are not displayed.")

# 5. Closing the browser
driver.quit()
