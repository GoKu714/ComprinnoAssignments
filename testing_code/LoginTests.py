import unittest
import HtmlTestRunner
from selenium import webdriver
import os

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://qa.tevi.co/login')


    def test_scenario1_incorrect_password_login(self):
        print("Inside test_scenario3_incorrect_password_login")
        self.pwd = "hello12345"
        # Find Login Tag
        self.login_el = self.driver.find_element_by_tag_name("login")
        # Find email within Login tag
        self.login_email_el = self.login_el.find_element_by_name("email")
        self.login_email_el.send_keys('vikram.dhoke@comprinno.net')

        # Find password within Login tag
        self.login_password_el = self.login_el.find_element_by_name("password")
        self.login_password_el.send_keys(self.pwd)

        # Click login button
        self.login_button_el = self.login_el.find_element_by_id("loginButton")
        self.login_button_el.submit()

    def test_scenario2_no_passwd_login(self):
        print("Inside test_scenario4_incorrect_password_login")
        self.pwd = ""
        # Find Login Tag
        self.login_el = self.driver.find_element_by_tag_name("login")
        # Find email within Login tag
        self.login_email_el = self.login_el.find_element_by_name("email")
        self.login_email_el.send_keys('vikram.dhoke@comprinno.net')

        # Find password within Login tag
        self.login_password_el = self.login_el.find_element_by_name("password")
        self.login_password_el.send_keys(self.pwd)

        # Click login button
        self.login_button_el = self.login_el.find_element_by_id("loginButton")
        self.login_button_el.submit()


if __name__ == '__main__':
    unittest.main()