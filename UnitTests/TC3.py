import unittest
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckingDescriptionOfAllPhonesFromCSV(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_all_phones_from_CSV_details_displayed(self):
        # 1. Opening the website https://www.demoblaze.com/index.html
        self.driver.get("https://www.demoblaze.com/index.html#")

        # 1. Choosing the category: Phones
        category_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        category_link.click()

        # 2. Reading phone names from the CSV file
        phone_names = []
        with open("phone_names.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                phone_names.append(row[0])

        # 3. Iterate over each phone names from the CSV file
        for phone_name in phone_names:
            # 3a. Clicking on the selected phone
            phone_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{phone_name}')]")))
            phone_item.click()

            # 3b. Verifying if the price and product description are displayed
            phone_price = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "price-container"))).text
            phone_description = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "more-information"))).text

            # 3c. Assert that both the price and product description are displayed
            self.assertTrue(phone_price and phone_description, f"Price and product description for {phone_name} are not displayed.")

            # 3d Going back to the Phones category page
            self.driver.execute_script("window.history.go(-1)")


if __name__ == '__main__':
    unittest.main()
