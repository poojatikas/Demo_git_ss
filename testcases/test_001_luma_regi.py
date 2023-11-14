import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_01_luma_regi():
    def test_01(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("https://magento.softwaretestingboard.com/customer/account/create/")

        driver.find_element(By.XPATH,'//input[@id="firstname"]').send_keys('Pooja')

        driver.find_element(By.XPATH,'//input[@id="lastname"]').send_keys('Tikas')

        driver.find_element(By.XPATH,'(//input[@type="email"])[1]').send_keys('poojatikas2@gmail.com')

        driver.find_element(By.XPATH,'(//input[@type="password"])[1]').send_keys('tikas@001')

        driver.find_element(By.XPATH,'//input[@title="Confirm Password"]').send_keys('tikas@001')

        driver.find_element(By.XPATH,'(//button[@class="action submit primary"])[1]').click()
        #
        time.sleep(2)

        if(driver.title=='My Account'):
            driver.save_screenshot('D:\\pythonProject1\\Revision\\screenshots\\test_01_pass.png')
            print('Registration is Successful')
            time.sleep(5)


        else:
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_01_fail.png")
            print('Registration is Unsuccessful')

        driver.close()


