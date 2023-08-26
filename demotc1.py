# we are selecting one way mumbai - dubai, selecting the date -> search flight -> selecting filtering all flights by 1 stop

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class AutoSelect():
    def oneStop(self):
        url = "https://yatra.com"
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        wait = WebDriverWait(driver, 50)
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//i[@class="countrylogo-uae"]').click()
        currency = driver.find_elements(By.CLASS_NAME,"sub-menu-dropdown")
        # print(currency)
        # print(len(currency))

        for results in currency:
            if "IND " == results.text:
                results.click()
                break

        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//a[@title="One Way"]').click()
        input = driver.find_element(By.XPATH,'//input[@name="flight_origin"]')
        input.click()
        driver.implicitly_wait(30)
        input.send_keys("pun")
        driver.implicitly_wait(20)
        Dep_city = driver.find_elements(By.CLASS_NAME, "origin_ac")

        for results in Dep_city:
            if 'Pune (PNQ)' == results.text:
                results.click()
                break

        arr_city = driver.find_element(By.XPATH,'//input[@id="BE_flight_arrival_city"]')
        driver.implicitly_wait(15)
        arr_city.click()
        driver.implicitly_wait(15)
        arr_city.send_keys('Duba')
        arrival = driver.find_elements(By.CLASS_NAME,"dest_ac")

        # print(len(arr_city))

        for results in arrival:
            if 'Dubai (DXB)' == results.text:
                results.click()
                break

    time.sleep(10)

AS = AutoSelect()
AS.oneStop()


