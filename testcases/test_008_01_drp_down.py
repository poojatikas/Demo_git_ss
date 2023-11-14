import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_08_Dropdown():
    def test_Drpdown(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.careinsurance.com/rhicl/proposalcp/renew/index-care")

        driver.find_element(By.XPATH,'//input[@id="policynumber"]').send_keys('12345669')
        time.sleep(1)

        driver.find_element(By.XPATH,'//input[@placeholder="DOB"]').click()

        month = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-month"]'))
        month.select_by_visible_text('Aug')
        time.sleep(1)

        year = Select(driver.find_element(By.XPATH,'//select[@class="ui-datepicker-year"]'))
        year.select_by_value('2023')
        time.sleep(1)

        driver.find_element(By.XPATH,'//a[text()="15"]').click()

        driver.find_element(By.XPATH,'//input[@placeholder="Contact Number"]').send_keys('9123457412')

        driver.save_screenshot('D:\\pythonProject1\\Revision\\screenshots\\test_08_Drpdown_pass.png')

        driver.close()




