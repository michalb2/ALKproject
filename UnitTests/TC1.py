import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckingDescriptionOfSelectedPhone(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_selected_phone_details_displayed(self):
        # 1. Opening the website: https://www.demoblaze.com/index.html
        self.driver.get("https://www.demoblaze.com/index.html#")

        # 2. Choosing the category: Phones
        category_link = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Phones")))
        category_link.click()

        # 3. Clicking on the selected phone : Samsung galaxy s6
        phone_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")))
        phone_name = phone_item.text
        phone_item.click()

        # 4. Verifying if the price and product description are displayed
        phone_price = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "price-container"))).text
        phone_description = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "more-information"))).text

        # Assert that both the price and product description are displayed
        self.assertTrue(phone_price and phone_description, f"Price and product description for {phone_name} are not displayed.")


if __name__ == '__main__':
    unittest.main()
