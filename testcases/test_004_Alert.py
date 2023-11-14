from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert



class Test_004_Alert():

    def test_04_alert(self):
        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

    #
        driver.get("https://nxtgenaiacademy.com/alertandpopup/")
        # #
        driver.find_element(By.XPATH,"//button[@name='alertbox']").click()

        msg1= Alert(driver).text
        print('\n Alert message=',msg1)
        #
        Alert(driver).accept()

        driver.close()


    def test_04_confirm(self):
        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

        #
        driver.get("https://nxtgenaiacademy.com/alertandpopup/")
        # #
        driver.find_element(By.XPATH,'//button[@name="confirmalertbox"]').click()

        msg2 = Alert(driver).text
        print('\n Confirm message:',msg2)

        Alert(driver).accept()
        Confirmaccept= driver.find_element(By.XPATH,'//p[@id="demo"]').text
        print('\n Confirm Alert Msg after accept')
        print(Confirmaccept)


        # Alert(driver).dismiss()
        # ConfirmDismiss = driver.find_element(By.XPATH,'//p[@id="demo"]').text
        # print('\n Confirm msg after dismiss')
        # print(ConfirmDismiss)

        driver.close()


    def test_04_Prompt(self):

        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        driver.maximize_window()

        #
        driver.get("https://nxtgenaiacademy.com/alertandpopup/")
        #
        driver.find_element(By.XPATH,'//button[@name="promptalertbox1234"]').click()

        msg3 = Alert(driver).text
        print('\n Prompt Message:',msg3)

        Alert(driver).send_keys('Yes')

        Alert(driver).accept()

        promptaccept = driver.find_element(By.XPATH,'//p[@id="demoone"]').text
        print('\n Prompt Alert Message after accept')
        print(promptaccept)

        driver.close()



