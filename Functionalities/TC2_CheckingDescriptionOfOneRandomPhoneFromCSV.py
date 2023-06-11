import csv
import random
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

# 3. Reading the phone names from the CSV file: phone_names.csv
phone_names = []
with open("phone_names.csv", "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        phone_names.append(row[0])

# 4. Selecting a random phone name from the CSV
selected_phone = random.choice(phone_names)

# 5. Clicking on the selected phone
phone_item = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{selected_phone}')]")))
phone_name = phone_item.text
phone_item.click()

# 6. Verifying if the price and product description are displayed
phone_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "price-container"))).text
phone_description = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "more-information"))).text

if phone_price and phone_description:
    print(f"Price and product description for {phone_name} are displayed.")
else:
    print(f"Price and product description for {phone_name} are not displayed.")

# 7. Closing the browser
driver.quit()
