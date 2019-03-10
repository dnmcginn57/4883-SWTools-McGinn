"""
David McGinn
4883-Software_tools
This program uses beautiful scraper to scrape emojis from the web
"""

from beautifulscraper import BeautifulScraper
import urllib
import sys
from time import sleep
from random import shuffle
import requests

scraper = BeautifulScraper()
url = 'https://www.webfx.com/tools/emoji-cheat-sheet/'
page = scraper.go(url)

delays = [.01,.02,.03,.04,.05]

i = 0
for emoji in page.find_all("span",{"class":"emoji"}):
    image_path = emoji['data-src']
    emoji_name = image_path.split("/")
    urllib.request.urlretrieve(url+image_path,'./emojis/'+emoji_name[2])
    shuffle(delays)
    sleep(delays[0])
    