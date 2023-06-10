from bs4 import BeautifulSoup
import selenium
import time

from test import driver

driver.webdriver.Chrome()
driver.get("https://tf.tfrrs.org/lists/4044/2023_NCAA_Division_I_All_Schools_Rankings?gender=m")

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find('table', {'class': 'allRows'})
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    athlete = columns[1].text.strip()
    year = columns[2].text.strip()
    school = columns[3].text.strip()
    time_val = columns[4].text.strip()
    print(f"Athlete: {athlete}, Year: {year}, School: {school}, Time: {time_val}")

driver.quit()