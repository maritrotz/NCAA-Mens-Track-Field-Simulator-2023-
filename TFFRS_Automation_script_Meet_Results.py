import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class TrackandField():
    def selectDropdown(self):
        options = Options()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get('https://www.tfrrs.org/')
        driver.maximize_window()
        links = driver.find_elements("xpath", "//a[@href]")
        for link in links:
            if "MEET RESULTS" in link.get_attribute("innerHTML"):
                link.click()
                break
        dropDown = driver.find_element(by=By.NAME, value="with_sports")
        dd = Select(dropDown)
        dd.select_by_visible_text("Track & Field")

        time.sleep(1)

        dropDown1 = driver.find_element(by=By.NAME, value="with_states")
        dd1 = Select(dropDown1)
        dd1.select_by_visible_text("CA")

        time.sleep(1)

        dropDown2 = driver.find_element(by=By.NAME, value="with_year")
        dd2 = Select(dropDown2)
        dd2.select_by_visible_text("2023")

        time.sleep(3)

        searchClick=driver.find_element(by=By.XPATH,value='//*[@id="results_filter"]/div/div[6]/p/button')
        searchClick.click()







dddemo = TrackandField()
dddemo.selectDropdown()



