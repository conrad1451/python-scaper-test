import mechanicalsoup
import pandas as pd
import sqlite3

my_link = "https://www.scrapethissite.com/pages/simple/"

browser = mechanicalsoup.StatefulBrowser()
browser.open(my_link)

#extract data
my_country_div = browser.page.find_all("div", attrs={"class": "col-md-4 country"})

# we use a list comprehension to isolate the text value of my country div
distribution = [value.text for value in my_country_div]
print(distribution)
