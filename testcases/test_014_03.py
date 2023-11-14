import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_014_Multiplication():

    def test_Mul(self):
        e=10
        f=15
        Mul=e*f
        if(Mul==150):
            print('\n VALID OPERATION')
            print("Result=",Mul)
            assert True
        else:
            print('\n INVALID OPERATION')
            assert False


    def test_014_03(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        driver.find_element(By.XPATH,"//a[contains(text(),'Sign In')]").click()

        driver.find_element(By.XPATH,"(//input[@type='email'])[1]").send_keys('poojatikas2@gmail.com')

        driver.find_element(By.XPATH,'//input[@title="Password"]').send_keys('tikas@001')
        time.sleep(2)

        driver.find_element(By.XPATH,'(//button[@type="submit"])[2]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,'(//button[@class="action switch"])[1]').click()

        driver.find_element(By.XPATH,'(//a[text() = "My Account"])[1]').click()

        if (driver.title== "My Account"):
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_014_03_pass.png")

            print('\n*********CONTACT INFORMATION********');
            text1 = driver.find_element(By.XPATH, '(//div[@class="box-content"])[1]').text;
            print(text1);

            text2 = driver.find_element(By.XPATH, '(//div[@class="box-content"])[2]').text;
            print("\n**********ADDRESS INFORMATION********");
            print(text2);

            driver.find_element(By.XPATH,"(//button[@class='action switch'])[1]").click()

            driver.find_element(By.XPATH,'//div[@aria-hidden="false"]//a[normalize-space()="Sign Out"]').click()

            driver.close()
            assert True

        else:
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_014_03_fail.png")

            print('\n*********NOT ABLE TO PRINT ACCOUNT INFORMATION')
            driver.close()
            assert False


















