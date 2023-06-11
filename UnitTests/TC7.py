import unittest
import csv
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker


class PurchasePhoneWithFakeData(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_purchase_phone(self):
        # 1. Opening the website https://www.demoblaze.com/index.html
        driver = self.driver
        driver.get("https://www.demoblaze.com/index.html")

        # 2. Selecting the category: Phones
        category_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        category_link.click()

        # 3. Reading phone names from the CSV file
        phone_names = []
        with open("phone_names.csv", "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                phone_names.append(row[0])

        # 4. Selecting a random phone from the CSV file
        selected_phone = random.choice(phone_names)

        # 5. Clicking on the selected phone
        phone_item = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{selected_phone}')]")))
        phone_item.click()

        # 6. Adding the phone to the cart
        add_to_cart_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Add to cart')]")))
        add_to_cart_button.click()

        # 7. Waiting for the cart modal to be displayed and showing the items in cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "cartur"))).click()
        time.sleep(3)

        # 8. Verifying if the chosen phone is added to the cart
        cart_items = driver.find_elements(By.XPATH, "//tbody//td[2]")
        phone_added = False
        for item in cart_items:
            if item.text == selected_phone:
                phone_added = True
                break

        self.assertTrue(phone_added, f"Failed to add {selected_phone} to the cart.")
        print(f"{selected_phone} is added to the cart successfully.")

        # 9. Choosing the action "Place Order"
        place_order_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]")))
        place_order_button.click()

        # 10. Filling in the form fields with fake values using Faker library
        fake = Faker()
        name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
        name_input.send_keys(fake.name())

        country_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "country")))
        country_input.send_keys(fake.country())

        city_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "city")))
        city_input.send_keys(fake.city())

        card_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "card")))
        card_input.send_keys(fake.credit_card_number())

        month_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "month")))
        month_input.send_keys(fake.random_int(min=1, max=12))

        year_input = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "year")))
        year_input.send_keys(fake.random_int(min=2023, max=2030))

        # 11. Clicking the "Purchase" button
        purchase_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Purchase')]")))
        purchase_button.click()

        # 12. Checking if the new popup with the text "Thank you for your purchase" is displayed
        popup_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert"))).text
        self.assertIn("Thank you for your purchase!", popup_text)
        print("The new popup with the text 'Thank you for your purchase' is displayed.")

if __name__ == "__main__":
    unittest.main()
