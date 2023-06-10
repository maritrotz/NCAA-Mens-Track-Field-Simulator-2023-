import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


class TrackandField():

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('https://www.tfrrs.org/')
        time.sleep(3)
        self.driver.maximize_window()
        self.df = pd.DataFrame(columns=['Athlete Name', 'Year', 'Team', 'Time'])

    def selectDropdown(self):
        performanceList = self.driver.find_element(by=By.XPATH, value="//span[normalize-space()='PERFORMANCE LISTS']")
        chains = ActionChains(self.driver)
        chains.move_to_element(performanceList).perform()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/ul/li[4]/ul/li[2]/a/span").click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value="//a[normalize-space()='2023 Div. I Combined List']").click()
        time.sleep(5)

        eventList = self.driver.find_element(by=By.NAME, value="event_type")
        eventselect = Select(eventList)
        eventselect.select_by_visible_text("1500 Meters")
        time.sleep(3)

        genderList = self.driver.find_element(by=By.NAME, value="gender")
        genderselect = Select(genderList)
        genderselect.select_by_visible_text("Men")
        time.sleep(3)

    def dataframecreation(self):

        athlete = self.driver.find_elements("xpath", '//td[@class ="tablesaw-priority-1"]')
        year = self.driver.find_elements("xpath", '//td[@ class ="tablesaw-priority-4"]')
        team = self.driver.find_elements("xpath", "//a[contains(@href, 'teams')]")
        timeval = self.driver.find_elements("xpath", "//a[contains(@href, 'results')]")

        athlete_list = []
        for a in range(len(athlete)):
            athlete_list.append(athlete[a].text)

        year_list = []
        for y in range(len(year)):
            year_list.append(year[y].text)

        team_list = []
        for t in range(len(team)):
            team_list.append(team[t].text)

        time_list = []
        for z in range(len(timeval)):
            time_list.append(timeval[z].text)

        time_values = [item for item in time_list if re.match(r'\d+:\d+\.\d+', item)]

        data_tuples = list(zip(athlete_list[0:], year_list[0:], team_list[0:],
                               time_values[0:]))  # list of each players name and salary paired together
        temp_df = pd.DataFrame(data_tuples, columns=['Athlete Name', 'Year', 'Team',
                                                     'Time'])  # creates dataframe of each tuple in list
        self.df = pd.concat([self.df, temp_df])  # appends to master dataframe

        self.df.to_csv(r'C:\Users\marit\Downloads\Top_100_NCAA_1500m', index=False, header=True)

dddemo = TrackandField()
dddemo.__init__()
dddemo.selectDropdown()
dddemo.dataframecreation()