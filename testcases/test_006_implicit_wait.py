import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_06_implicit_wait():
    def test_implicit(self):
        driver = webdriver.Chrome()

        driver.implicitly_wait(35)

        driver.maximize_window()

        driver.get("https://www.google.com")

        driver.find_element(By.XPATH,'//textarea[@jsname="yZiJbe"]').send_keys('Internert speed')

        driver.find_element(By.XPATH,'(//input[@class="gNO89b"])[1]').click()

        driver.find_element(By.XPATH,'//div[text()="RUN SPEED TEST"]').click()
        time.sleep(20)

        driver.save_screenshot('D:\\pythonProject1\\Revision\\screenshots\\test_06_implicit.png')
        time.sleep(35)

        upload=driver.find_element(By.XPATH,'//p[@jsname="dSdcdd"]').text
        print('****Upload Speed****')
        time.sleep(7)
        print(upload + 'MBPS')

        Download=driver.find_element(By.XPATH,'//p[@jsname="Lk0VKd"]').text
        print('****Download Speed****')
        time.sleep(7)
        print(Download + 'MBPS')


        driver.close()



