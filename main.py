import mechanicalsoup
import pandas as pd
import sqlite3

my_link = ""

browser = mechanicalsoup.StatefulBrowser()
browser.open(my_link)
