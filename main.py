# better_country_scraper.py

# Sources: 
# [1]: https://stackoverflow.com/questions/522563/how-to-access-the-index-value-in-a-for-loop
# [2]: https://realpython.com/python-sleep/

import mechanicalsoup
import pandas as pd
import sqlite3

import time

my_link = "https://www.scrapethissite.com/pages/simple/"

browser = mechanicalsoup.StatefulBrowser()
browser.open(my_link)

def scrape_data(html_tag, class_name, newline_replacer):
  #extract data
  the_info = browser.page.find_all(html_tag, attrs={"class": class_name})
  distribution1 = [value.text.replace("\n", newline_replacer) for value in the_info]
  time.sleep(2) #[2]
  return distribution1


def value_checker(distribution_to_check):
  # [1]
  for index, val in enumerate(distribution_to_check):
    print("index", str(index), "has value")
    print(str(val))
    print("\n\n\n")


def play_game(data):
  while(True):
    print("Press a key to continue")
    time.sleep(2)

country_names = scrape_data("h3", "country-name", "")
# country_infos = scrape_data("div", "country-info", "|||")
country_capitals = scrape_data("span", "country-capital", "|||")
country_population = scrape_data("span", "country-population", "|||")
country_area = scrape_data("span", "country-area", "|||")

value_checker(country_capitals)
# value_checker(country_population)
# value_checker(country_area)

the_game_data_matrix = [[],[],[],[]]

the_game_data_matrix[0] = country_names
the_game_data_matrix[1] = country_capitals
the_game_data_matrix[2] = country_population
the_game_data_matrix[3] = country_area


play_game(the_game_data_matrix)

# for i in range(len(distribution)):
#   # curData = distribution[i][0]
#   curData = distribution[i]
#   # print("curData is ", curData)
#   print("curData lenght is", str(len(curData)))
#   the_game_data_matrix[i%4].append(curData)



# my_print_target = the_game_data_matrix[0]
# print(my_print_target)
# print("\n\n\n\n SPACER \n\n\n\n")
# my_print_target = the_game_data_matrix[1]
# print(my_print_target)
# print("\n\n")

# for elem in my_print_target:
  # print(elem)
  # print("\n")
