import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class window(unittest.TestCase):
    def setUp(self):
        serv_obj=Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        time.sleep(5)

    def test_main_Window(self):
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(10)
        self.main_window=self.driver.current_window_handle
        self.driver.switch_to.new_window()
        self.driver.get("https://demo.nopcommerce.com/")
        self.windows=self.driver.window_handles
        print(self.windows)
        self.driver.switch_to.window(self.windows[1])
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
        time.sleep(5)
        self.driver.switch_to.window(self.main_window)
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//input[@id='name']").send_keys("veeresh")
        time.sleep(4)
    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()

