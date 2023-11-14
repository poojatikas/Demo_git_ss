import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_014_Substraction():

    def test_sub(self):
        c=10
        d=5
        sub=(c-d)
        if (sub==5):
            print('\n SUBSTRACTION SUCESSFUL')
            print("Result=",sub)
            assert True
        else:
            print('\n SUBSTRACTION UNSUCESSFUL')
            assert False


    def test_014_002(self):

        driver= webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH, "//div[@class='panel header']//a[contains(text(),'Sign In')]").click()

        driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('poojatikas2@gmail.com')

        driver.find_element(By.XPATH, '//input[@title="Password"]').send_keys('tikas@001')

        driver.find_element(By.XPATH, '//span[text()="Sign In"]').click()
        time.sleep(2)

        try:
            driver.find_element(By.XPATH, '(//span[@class="logged-in"])[1]');

            driver.save_screenshot('D:\\pythonProject1\\Revision\\screenshots\\test_014_02_login_pass.png');

            print("\n*********LOGIN SUCCESSFUL*******");

            driver.find_element(By.XPATH, "//div[@class='panel header']//button[@type='button']").click();

            driver.find_element(By.XPATH, '(//a[contains(text(),"Sign Out")])[1]').click();

            driver.close();

            assert True;

        except:
            driver.save_screenshot('D:\\pythonProject1\\Revision\\screenshots\\test_014_02_login_fail.png');

            print('\n********LOGIN UNSUCCESSFUL********');

            driver.close();

            assert False;









































































































































































