from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class chrome_driver:

    def set(self):
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return chrome_driver
    pass


class selenium_data_scripting_test:
    def start(self):
        url = "http://automationpractice.com/index.php?id_category=3&controller=category"

        driver = chrome_driver.set(self)
        driver.get(url)