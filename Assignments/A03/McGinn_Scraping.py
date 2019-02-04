from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
import json
import sys
from time import sleep
from random import shuffle

scraper = BeautifulScraper()



years = [x+1 for x in range(1969,2019)] 
stype = ""
weeks = [x+1 for x in range(18)]

delays = [.01,.02,.03,.04,.05]
#url = "http://www.nfl.com/schedules/%d/%s%s" % (sYear,stype,str(week))
#url2 = "http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"

gameIDs = []
#iterate for every year
for year in years:
    print(year)
    #iterate every week in a given year
    for week in weeks:
        url = "http://www.nfl.com/schedules/%d/REG%s" % (year,str(week))
        page = scraper.go(url)
        print(week)
        #all divs with the data-gameid in them
        idDivs = page.find_all("div", {'class':'schedules-list-content'})
        #a ham-fisted and stupid way to fix this problem
        #idDivsAlt = page.find_all("div", {'class':'schedules-list-content post expandable primetime type-reg pro-legacy'})
        #idDivsAlt2 = page.find_all("div", {'class':'schedules-list-content post expandable type-reg pro-legacy'})
        #add all the found game id's to gameIDs[]
        for div in idDivs:
            gameIDs.append(div['data-gameid'])
            print(".")
        #for div in idDivsAlt:
        #    gameIDs.append(div['data-gameid'])
        #    print(".")
        #for div in idDivsAlt2:
        #    gameIDs.append(div['data-gameid'])
        #    print(".")
    
    #now just do post season id's by themselves for each year
    url = "http://www.nfl.com/schedules/%d/POST" % (year)
    page = scraper.go(url)
    idDivs = page.find_all("div", {'class':'schedules-list-content'})
    #idDivsAlt = page.find_all("div", {'class':'schedules-list-content post expandable primetime type-reg pro-legacy'})
    #idDivsAlt2 = page.find_all("div", {'class':'schedules-list-content post expandable type-reg pro-legacy'})
    #add all the found game id's to gameIDs[]
    for div in idDivs:
        gameIDs.append(div['data-gameid'])
   
    #for div in idDivsAlt:
    #    gameIDs.append(div['data-gameid'])

    #for div in idDivsAlt2:
    #    gameIDs.append(div['data-gameid'])
        
        

print(len(gameIDs))

#after much debugging, it is determined gameIDs has the right number of game id's in it

#generate urls for live update from id's in gameIDs and consolidate them into a single json file



