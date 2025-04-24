import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


class Day2(unittest.TestCase):

    def setUp(self):
        self.serv_obj = Service("C:\webdrivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()

    def test_handle_dropdown(self):
        self.dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='country']"))
        self.dropdown.select_by_index(5)
        time.sleep(10)

    def test_handle_checkbox(self):
        self.checkboxes = self.driver.find_elements(By.XPATH, "//input[@class='form-check-input']")

        # Loop through all checkboxes
        for checkbox in self.checkboxes:
            # Find the associated label using the 'for' attribute to match the checkbox
            label = self.driver.find_element(By.XPATH, f"//label[@for='{checkbox.get_attribute('id')}']")

            # Check if the label's text matches "Wednesday"
            if label.text.lower() == "wednesday":
                checkbox.click()

        time.sleep(10)

    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    def test_date_picker(self):
        self.mon = "November"
        self.date = "25"

        # Locate the datepicker input field and click it to open the calendar
        self.driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

        while True:
            # Get the current month and year
            month = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
            year = self.driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

            # Break if the desired month and year are found
            if year == "2026" and month == self.mon:
                break
            else:
                # Click the "next" button to go to the next month
                self.driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()

            # Wait for the calendar to update after clicking the "next" button

        # Locate all the dates in the calendar and select the correct one
        dates = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td")
        for day in dates:
            if day.text == self.date:
                day.click()
                break

        # Wait for 10 seconds to observe the result (if needed)
        time.sleep(10)
    def test_handle_simple_alert(self):
        self.driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
        self.alert=self.driver.switch_to.alert
        print(self.alert.text)
        self.alert.accept()
        time.sleep(10)
    def test_handle_textbox_alert(self):
        self.driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
        self.text_alert=self.driver.switch_to.alert
        self.text_alert.send_keys("Hi Veeresh")
        self.text_alert.accept()
        time.sleep(10)



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
