from selenium import webdriver

class Test_013_mousescroll():

    def test_013_scroll(self):
        driver = webdriver.Chrome()

        driver.maximize_window()

        driver.implicitly_wait(5)

        driver.get("https://www.bbc.com/news")

        driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_013_mousescroll_pass.png")

        driver.execute_script("window.scrollBy(0,1000)")

        driver.save_screenshot("D:\\pythonProject1\\Revision\\screenshots\\test_013_mouse_scroll_pass.png")

        driver.close()

