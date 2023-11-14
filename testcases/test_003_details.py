import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_03_luma_detals():

    def test_03_account_details(self):

        driver=webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('poojatikas2@gmail.com')

        driver.find_element(By.XPATH, '//input[@title="Password"]').send_keys('tikas@001')

        driver.find_element(By.XPATH, '//span[text()="Sign In"]').click()

        if(driver.title=='Home Page'):
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_03_details_pass.png")
            driver.find_element(By.XPATH,"//div[@class='panel header']//button[@type='button']").click()
            time.sleep(2)

            driver.find_element(By.XPATH,"//div[@aria-hidden='false']//a[normalize-space()='My Account']").click()

            info=driver.find_element(By.XPATH,'//p[contains (text(),"Pooja Tikas")]').text
            print("Account Details")
            print(info)

            address = driver.find_element(By.XPATH,"(//address[contains(text(),'Pooja Tikas')])[1]").text
            print('\n Address')
            print(address)

            driver.find_element(By.XPATH,"//div[@class='panel header']//button[@type='button']").click()

            driver.find_element(By.XPATH,"//div[@aria-hidden='false']//a[normalize-space()='Sign Out']").click()

            driver.close()

            assert True

        else:
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_03_details_fail.png")

            driver.close()

            assert False











