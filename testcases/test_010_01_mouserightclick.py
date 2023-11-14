import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class Test_010_mouserightclick():

    def test_10_rightclick(self):

        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/mouseevent/")

        action = ActionChains(driver)

        right_click = driver.find_element(By.XPATH,'//button[@id="rightclick"]')

        action.context_click(right_click).perform()

        driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_010_mouserightclick_pass.png")

        driver.find_element(By.XPATH,'//a[text()="Registration Form"]').click()
        time.sleep(1)
        #
        text = driver.find_element(By.XPATH,'//div[@class="copyright_text"]').text
        print('\n*********TEST AFTER RIGHT CLICK**********')
        print(text)

        driver.close()
