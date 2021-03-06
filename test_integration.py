import time
import unittest
import os
import logging
from app import app

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class IsAppUp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        print("In setUp")
        caps = {'browserName': 'chrome'}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps)
        self.logger = logging
        self.logger.info("About to call a test")

    def test_simple(self):
        print("In simple")
        self.logger.info("In simple")
        browser = self.browser
        browser.get('http://localhost:5004/interviews')
        time.sleep(3)
        """ self.assertIn("Home", browser.title)
        search_box = browser.find_element_by_name('employeeName')
        search_box.send_keys('John')
        search_box.send_keys(Keys.RETURN)
        time.sleep(3) # simulate long running test
        self.assertIn('John', browser.page_source) """
    
    def test_page(self):
        response = self.app.get('/interviews', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        print("In tearDown")
        self.browser.quit() # quit vs close?


if __name__ == '__main__':
    logging.basicConfig(filename='selenium-plugin.log',level=logging.INFO)
    logging.info("About to call main")
    unittest.main()
