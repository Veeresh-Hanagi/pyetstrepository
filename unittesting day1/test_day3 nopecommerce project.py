import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

class nopecommerce(unittest.TestCase):
    def setUp(self):
        self.serv_obj=Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://demo.nopcommerce.com/")
        self.driver.maximize_window()


    def test_validate_register_function(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Register']").click()
        time.sleep(10)
        self.pagetitle=self.driver.title
        if self.pagetitle=="Just a moment...":
            self.driver.find_element(By.XPATH,"//*[@id='DPxlC8']/div/label/input").click()
            time.sleep(10)
        if self.pagetitle=="Just a moment...":
            self.driver.find_element(By.XPATH,"//*[@id='DPxlC8']/div/label/input").click()
            time.sleep(10)
        self.driver.find_element(By.XPATH,"//input[@id='gender-male']").click()
        self.driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Veeresh")
        self.driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys("Hanagi")
        self.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("veereshahangi1098@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Pass@1098")
        self.driver.find_element(By.XPATH,"//input[@id='ConfirmPassword']").send_keys("Pass@1098")
        self.driver.find_element(By.XPATH,"//button[@id='register-button']").click()
        time.sleep(10)



    def test_validate_login_function(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Log in']").click()
        time.sleep(10)
        if self.driver.title=="Just a moment...":
            self.driver.find_element(By.XPATH,"//*[@id='DPxlC8']/div/label/input").click()
        if self.pagetitle=="Just a moment...":
            self.driver.find_element(By.XPATH,"//*[@id='DPxlC8']/div/label/input").click()
            time.sleep(10)
        self.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("veereshahangi1098@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys("Pass@1098")
        self.driver.find_element(By.XPATH,"//input[@id='RememberMe']").click()
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
        time.sleep(10)


    def tearDown(self):
        self.driver.quit()
