import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_08_Facebook_drpdown():
    def test_08_drp(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.facebook.com")

        driver.find_element(By.XPATH,'//a[@rel="async"]').click()

        driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys('Dimpal')

        driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys('Malve')

        driver.find_element(By.XPATH,'//input[@aria-label="Mobile number or email address"]').send_keys('9256412143')

        driver.find_element(By.XPATH,'//input[@autocomplete="new-password"]').send_keys('124578112')
        time.sleep(5)

        day = Select(driver.find_element(By.XPATH,'//select[@id="day"]'))
        day.select_by_value('9')

        month = Select(driver.find_element(By.XPATH,'//select[@id="month"]'))
        month.select_by_index('5')

        year = Select(driver.find_element(By.XPATH, '//select[@id="year"]'))
        year.select_by_value('2023')

        driver.find_element(By.XPATH,'(//label[@class="_58mt"])[1]').click()
        time.sleep(2)

        driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_08_fbdrp_pass.png")

        driver.close()
















