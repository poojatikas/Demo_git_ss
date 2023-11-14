import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_07_explicit():
    def test_Ex_wait(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH,"//textarea[@jsname='yZiJbe']").send_keys('Internet speed test')
        time.sleep(5)

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()
        time.sleep(5)

        driver.find_element(By.XPATH,'//div[text()="RUN SPEED TEST"]').click()
        time.sleep(2)

        try:
            wait = WebDriverWait(driver,30, poll_frequency=0.5)
            wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//div[text()="TEST AGAIN"]')))

            time.sleep(5)
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_07_explicit_pass.png")
            time.sleep(5)

            uploadspeed = driver.find_element(By.XPATH,"//p[@jsname='dSdcdd']").text
            print('\n****** upload speed*****')
            print(uploadspeed + 'MBPS')


            Downloadspeed = driver.find_element(By.XPATH,"//p[@jsname='Lk0VKd']").text
            print('\n**** Download Speed*****')
            print(Downloadspeed + 'MBPS')

            driver.close()
            assert True

        except:
            print('*****some error Occured***')
            driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_07_explicit_fail.png")
            driver.close()
            assert False



