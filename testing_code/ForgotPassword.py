import unittest
import HtmlTestRunner
from selenium import webdriver
import os

class FogotPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://qa.tevi.co/login')

    def test_click_forgot_password(self):
        print("Inside test_click_forgot_password")
        # Find Login Tag
        self.login_el = self.driver.find_element_by_tag_name("login")
        # Find email within Login tag
        new_link = self.driver.find_element_by_id("forgotPassword").get_attribute("href")
        self.login_email_el = self.login_el.find_element_by_id("forgotPassword").click()
        # window_before = self.driver.window_handles[0]


if __name__ == '__main__':
    unittest.main()