import mechanicalsoup
import pandas as pd
import sqlite3

my_link = ""

browser = mechancialsoup.StatefulBrowser()
browser.open(my_link)
