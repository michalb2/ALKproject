import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAboutUsVideo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_play_about_us_video(self):
        # 1: Opening the website https://www.demoblaze.com/index.html
        driver = self.driver
        driver.get("https://www.demoblaze.com/index.html")

        # 2: Clicking on the tab: "About us"
        about_us_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "About us")))
        about_us_link.click()

        # 3: Waiting for the video player modal to be displayed
        video_modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "videoModal")))

        # 4: Playing the video
        video_player = WebDriverWait(video_modal, 10).until(EC.presence_of_element_located((By.ID, "example-video_html5_api")))
        driver.execute_script("arguments[0].play();", video_player)

        # 5: Waiting for the video
        time.sleep(3)

        # 6: Closing the video modal
        close_button = WebDriverWait(video_modal, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "close")))
        close_button.click()


    if __name__ == "__main__":
        unittest.main()
