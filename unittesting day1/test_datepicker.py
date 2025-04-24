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

    def test_handledatepicker(self):
        self.driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys("08-08-2000")
        self.driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys("19-04-2025")
        self.driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()
        time.sleep(10)
        self.result=self.driver.find_element(By.XPATH,"//div[@id='result']").text
        if self.result=="You selected a range of 9020 days.":
            print("test case passed ")
        else:
            print("test case failed")
    def test_validatedatepicker(self):
        self.driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
        while True:
            month="January"
            day="8"
            year="2027"
            mon=self.driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
            yrr=self.driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
            if yrr==year and mon==month:
                break
            else:
                self.driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

        dates=self.driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")

        for date in dates:
             if date.text==day:
                date.click()
        time.sleep(10)



    def tearDown(self):
        self.driver.close()
