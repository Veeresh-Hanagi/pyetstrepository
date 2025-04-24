import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium import webdriver

import time

class handlescrollbar(unittest.TestCase):
    def setUp(self):
        self.serv_obj=Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(5)
    def test_scrollbyvalue(self):
        self.driver.execute_script("window.scrollBy(0,1000)"," ")
        time.sleep(5)

    def test_scrolluntillelement(self):
        self.elemnet=self.driver.find_element(By.XPATH,"//h2[normalize-space()='Upload Files']")
        self.driver.execute_script("arguments[0].scrollIntoView();",self.elemnet)
        time.sleep(5)
    def test_scrolltilllast(self):
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
        time.sleep(5)


    def tearDown(self):
        self.driver.quit()
