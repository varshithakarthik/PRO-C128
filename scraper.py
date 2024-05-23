from bs4 import BeautifulSoup
import time
# rows and columns
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"
headers = ["name", "year_discovered", "discoverer", "distance_from_planet (km)", "diameter (km)", "orbital_period", "host_planet"]
moons_data = []
# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scrapped_data = []

def scrape():
    bright_star_table = soup.find("table",attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all("tr")
    for row in table_rows: 
        table_cols = row.find_all('td')
        temp_list = []
        print(table_cols)
        for col_data in table_cols:
            data = col_data.text.strip()
            print(data)
            temp_list.append(data)
    scrapped_data.append(temp_list)

stars_data = []
for i in range(0,len(scrapped_data)):
    Star_name = scrapped_data[i][1]
    Distance = scrapped_data[i][3]
    Mass = scrapped_data[1][5]
    Radius = scrapped_data[i][6]
    Lum = scrapped_data[i][7]

    required_data = [Star_name, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)
    headers = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity']
    star_df_1 = pd.DataFrame(stars_data,columns=headers)
    star_df_1.to_csv('scrapped_data.csv',index=True,index_label="id")