from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_014_addition():

    def test_add(self):
        a=10
        b=20
        add=(a+b)
        if (add==30):
            print('\n ADDITION SUCESSFUL')
            print("Result=",add)
            assert True
        else:
            print('\n ADDITION UNSUCESSFUL')
            assert False


    def test_014_02(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://magento.softwaretestingboard.com/")

        if(driver.title == "Home Page"):
            print('\n***********YOU ARE AT HOME PAGE**********')
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_014_02_pass.png")
            driver.close()
            assert True

        else:
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_014_02_fail.png")
            print('\n********YOU ARE AT WRONG PAGE**********')
            driver.close()
            assert False



