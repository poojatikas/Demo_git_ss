import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class Test_014_Division():

    def test_014_01_Div(self):
        g = 15
        h = 5
        div = g / h
        if (div == 3):
            print('VALID OPERATION')
            print("Result=",div)
            assert True
        else:
            print('INVALID OPERATION')
            assert False

    def test_014_04_details(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)

        driver.find_element(By.XPATH,'//a[@title="Fusion Backpack"]').click()
        time.sleep(5)

        if(driver.title=="Fusion Backpack"):
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_014_04_pass.png")

            text1 = driver.find_element(By.XPATH,"(//div[@class='value'])[2]").text
            print('\n********PRODUCT DISCRIPTION**********')
            print(text1)

            driver.close()
            assert True

        else:

            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_014_04_fail.png")

            print('\n********NOT ABLE PROCESS YOUR REQUEST**********')

            driver.close()
            assert False








