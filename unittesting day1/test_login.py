import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class searchengine(unittest.TestCase):
    def test_google_search(self):
        self.serv_obj=Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://www.google.com/")
        print("title of the page is :" + self.driver.title)
        self.driver.close()
    def test_automation_testing_blogspot(self):
        self.serv_obj = Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        print("title of the page is :" + self.driver.title)
        self.driver.close()


if __name__=="__main__":
    unittest.main()