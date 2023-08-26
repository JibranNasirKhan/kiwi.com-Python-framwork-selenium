from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Search_flights():
    def flight_results(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.akbartravels.com/")
        driver.maximize_window()

        # selecting the Deparure city
        depart_city = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li[id='liFrom'] h6[class='ng-tns-c8-3']")))
        depart_city.click()
        depart_city = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mat-input-3")))
        depart_city.click()
        depart_city.send_keys("Mum")
        depart_city.send_keys(Keys.ENTER)

        # depart_city = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[@fxlayoutalign='space-between center'])[1]")))\
        #     .find_elements(By.XPATH,"(//a[@fxlayoutalign='space-between center'])[1]")
        # depart_city.click()

        # selecting the arrival city
        arr_city = driver.find_element(By.XPATH, "(//h6[normalize-space()='Chennai'])[1]")
        arr_city.click()
        arr_city.send_keys("Mum")
        arr_city.send_keys(Keys.ENTER)


Run = Search_flights()
Run.flight_results()