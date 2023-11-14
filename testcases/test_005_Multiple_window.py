import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_05_Multiple_window():

    def test_05_01_mul_window_handles(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/multiplewindows/")

        parenttext = driver.find_element(By.XPATH,'// h1[ @class ="elementor-heading-title elementor-size-default"]').text
        print('\n Parent Text Tab')
        print(parenttext)

        driver.find_element(By.XPATH,"//button[@name='145newbrowsertab234']").click()
        
        select_window = driver.window_handles
        
        driver.switch_to.window(select_window[1])

        childtext=driver.find_element(By.XPATH, '(//h2[@class="elementor-heading-title elementor-size-default"])[1]').text;
        print('\n CHILD TAB TEXT');
        print(childtext);
        time.sleep(5)

        driver.close()

        driver.switch_to.window(select_window[0])

        parenttext = driver.find_element(By.XPATH,
                                         '//h1[@class="elementor-heading-title elementor-size-default"]').text
        print('\n***PARENT TAB TEXT***')
        print(parenttext)
        driver.close()


    def test_05_02_mul_wndow_handle(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://nxtgenaiacademy.com/multiplewindows/")

        print('\n ****Parent Window Title***')

        parenttitle = driver.title

        print(parenttitle)

        parenttext2 = driver.find_element(By.XPATH,'//h1[@class="elementor-heading-title elementor-size-default"]').text
        print('\n ** parent window Text **')
        print(parenttext2)

        parent_window = driver.current_window_handle

        driver.find_element(By.XPATH, '//button[@name="newbrowserwindow123"]').click()

        select_window2 = driver.window_handles

        for w in select_window2:
            driver.switch_to.window(w)
            if(driver.title == 'NxtGen A.I Academy – Automate Intelligently' ):

                print('\n **Child Window Title**')
                childtitle = driver.title
                print(childtitle)

                print('\n ****Child Window Text***')
                childtext3 = driver.find_element(By.XPATH,'(//h2[@class="elementor-heading-title elementor-size-default"])[1]').text
                print(childtext3)

                driver.close()

                break

        driver.switch_to.window(parent_window)

        print('\n ****Parent Window Title')
        parenttitle2 = driver.title
        print(parenttitle2)

        parenttext3 = driver.find_element(By.XPATH,'//h1[@class="elementor-heading-title elementor-size-default"]').text
        print('\n ***Parent Window Text***')
        print(parenttext3)


        # driver.close()
        driver.quit()




