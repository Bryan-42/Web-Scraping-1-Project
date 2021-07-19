from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/bryancastro/Desktop/Coding/Web Scraping/chromedriver")
browser.get(START_URL)
time.sleep(10)

def Scrape():
    headers = ["name", "distance", "mass", "radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("td"):
        td_tags = tr_tag.find_all("td")
        star_list = []
        for index, td_tag in enumerate(td_tags):
            if index == 0:
                star_list.append(td_tag.find_all("a")[0].contents[0])
            else:
                try:
                    star_list.append(td_tag.contents[0])
                except:
                    star_list.append("")
        star_data.append(star_list)
    with open("Scraper.csv", "a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(star_data)

Scrape()