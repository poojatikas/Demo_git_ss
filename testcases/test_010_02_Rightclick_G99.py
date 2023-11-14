from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains



class Test_010_mouserightclick():

    def test_010_rightaction(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get(" https://demo.guru99.com/test/simple_context_menu.html")

        right_click=driver.find_element(By.XPATH, '//span[text()="right click me"]')

        action = ActionChains(driver)

        action.context_click(right_click).perform()

        driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_010_mouserightclick_g99_pass.png")

        driver.find_element(By.XPATH,"//span[text()='Edit']").click()

        alerttext = Alert(driver).text
        print('\n******AFTER RIGHT CLICK*******')
        print(alerttext)

        Alert(driver).accept()

        driver.close()



