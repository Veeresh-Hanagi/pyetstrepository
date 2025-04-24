from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import unittest
import time

class skiptest(unittest.TestCase):
    def setUp(self):
        self.serv_obj=Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()
        time.sleep(10)
    def tearDown(self):
        self.driver.quit()

    def test_simplealert(self):
        self.driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
        self.alert=self.driver.switch_to.alert
        time.sleep(5)
        self.alert.accept()
        time.sleep(5)
    def test_confiramtionalert(self):
        self.element=self.driver.find_element(By.XPATH,"//h2[normalize-space()='Alerts & Popups']")
        self.driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
        self.confirmation=self.driver.switch_to.alert
        time.sleep(5)
        validate=self.confirmation.text
        print(validate)
        self.assertEqual("Press a button!",validate,"the aleert is different")
        self.assertNotEqual("Press a button!123",validate)
        self.confirmation.dismiss()
    @unittest.skip (" i am skipping this method")
    def test_prompt_alert(self):
        self.driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
        self.prompt=self.driver.switch_to.alert
        time.sleep(10)
        print(self.prompt.text)
        self.prompt.send_keys("hi veeresh")
        self.prompt.accept()
        time.sleep(10)
if __name__=="__main__":
    unittest.main()





