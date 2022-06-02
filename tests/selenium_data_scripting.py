from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from colorama import Fore, Style

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

        # Get all listed products
        product_containers = driver.find_elements(By.CLASS_NAME, "product-container")

        for index,product_container in enumerate(product_containers):

            # Make hover action for see product price and details
            hover_action = ActionChains(driver).move_to_element(product_container)
            hover_action.perform()

            # selenium path indexi 0 dan değil 1 den başlıyor, bu yüzden index+1 verdim
            driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span' % (index+1)).click()
            item_name = driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li[%s]/div/div[2]/h5/a' % (index+1)).text

            cont_shopping_button = driver.find_element(By.CSS_SELECTOR, ".continue.btn.btn-default.button.exclusive-medium")

            # element bir süre sonra gözüktüğü için sync error almamak,
            # ve ürünün eklendiğini doğrulamak adına explicit wait kullandım
            try:
                element_visible = EC.visibility_of_element_located((By.CSS_SELECTOR, ".continue.btn.btn-default.button.exclusive-medium"))
                WebDriverWait(driver, 5).until(element_visible)

            except TimeoutException:
                raise Exception("Timed out waiting for item load, Test Failed")

            finally:
                cont_shopping_button.click()
                print(f"{Fore.GREEN}[PASS]{Style.RESET_ALL} Product Added: %s" % index + " - Item Name: %s" % item_name)
