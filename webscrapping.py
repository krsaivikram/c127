from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv
starturl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/Manorama/Desktop/c127/chromedriver")
browser.get(starturl)
time.sleep(10)
def Scrap():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(0,437):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tags in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv","w") as f:
        csvwriter = csv.writer(f)
        csv.writer.writerow(headers)
        csv.writer.writerows(planet_data)
Scrap()

                    
