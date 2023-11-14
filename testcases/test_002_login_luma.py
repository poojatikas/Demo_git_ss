import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_02_login_luma():
    def test_02_luma(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH,"//div[@class='panel header']//a[contains(text(),'Sign In')]").click()

        driver.find_element(By.XPATH,'//input[@id="email"]').send_keys('poojatikas2@gmail.com')

        driver.find_element(By.XPATH,'//input[@title="Password"]').send_keys('tikas@001')

        driver.find_element(By.XPATH,'//span[text()="Sign In"]').click()
        time.sleep(2)

        if(driver.title=='Home Page'):
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_02_luma_pass.png")
            print('Login Suceessfully')
            text12=driver.find_element(By.XPATH,'//span[text()="Sign In"]').text


            driver.find_element(By.XPATH,'(//button[@type="button"])[1]').click()
        #
            driver.find_element(By.XPATH,"//div[@aria-hidden='false']//a[normalize-space()='Sign Out']").click()
        #
            driver.close()
            assert True
        #
        else:
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_21_02_fail_luma.png")
            print("Login Unsucessfully")
            driver.close()
            assert False













