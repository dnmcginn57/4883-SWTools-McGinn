from beautifulscraper import BeautifulScraper
from pprint import pprint
import urllib
import json
import sys
import requests
from time import sleep
from random import shuffle
scraper = BeautifulScraper()



years = [x+1 for x in range(2008,2019)] 
stype = ""
weeks = [x+1 for x in range(18)]

delays = [.01,.02,.03,.04,.05]

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
        #add all the found game id's to gameIDs[]
        for div in idDivs:
            gameIDs.append(div['data-gameid'])
            print(".")

    
    #now just do post season id's by themselves for each year
    url = "http://www.nfl.com/schedules/%d/POST" % (year)
    page = scraper.go(url)
    idDivs = page.find_all("div", {'class':'schedules-list-content'})

    #add all the found game id's to gameIDs[]
    for div in idDivs:
        gameIDs.append(div['data-gameid'])
        
        
#gameIDs is 2680 which I think is a good number
print(len(gameIDs))

#now to access all of the live data sites and save them for later use

url = "http://www.nfl.com/liveupdate/game-center/%s/%s_gtd.json"


for gid in gameIDs:
    gameData = requests.get(url % (str(gid), str(gid)))
    gDataJSON = gameData.json()
    filePath = "./game_data/%s.json" % (str(gid))
    shuffle(delays)
    sleep(delays[1])
    with open(filePath, 'w') as fp:
        json.dump(gDataJSON,fp)

