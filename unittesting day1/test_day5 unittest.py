import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import  unittest
from selenium.webdriver.support.select import Select


class day3(unittest.TestCase):
    def setUp(self):
        serv_obj=Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(5)

    def handledatepicker(self):
        self.driver.find_element(By.XPATH,"//input[@id='start-date']").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


