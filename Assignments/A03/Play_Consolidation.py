"""
This file consolidates all plays into a single json
assumes folder play_data is exists
"""
import os, sys
import json
import pprint as pp
import ujson

"""
create a list of files
"""
def getFiles(path):
    files = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirname,filename))

    return files

"""
check to make sure is json
"""

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

"""
Try to open a file
"""
def openFileJson(path):
    try:
        f = open(path, "r")
        data = f.read()
        if is_json(data):
            return json.loads(data)
        else:
            print ("Error: Not Json")
            return {}
    except IOError:
        print ("Error: Game file doesn't exist.")
        return {}

path  = './game_data'
files = getFiles(path)

files = sorted(files)

toJson = {
    "2009" : {},
    "2010" : {},
    "2011" : {},
    "2012" : {},
    "2013" : {},
    "2014" : {},
    "2015" : {},
    "2016" : {},
    "2017" : {},
    "2018" : {},
}
season = -1
for file in files:
    #start making some dictionaries
    data = openFileJson(file)

    #pull out game id and game data
    for gameid,gamedata in data.items():
        #account for the other high-level tag
        if gameid != 'nextupdate':
            #set correct season based on ID
            if int(gameid[4:6]) < 3:
                season = int(gameid[:4]) - 1
            else:
                season = int(gameid[:4])
            #we only really care about the drives
            for driveid,drivedata in gamedata['drives'].items():
                #crntdrv is redundant
                if driveid != 'crntdrv':
                    for playid,playdata in drivedata['plays'].items():
                        print(playid)
                        toJson[str(season)].update({playid : playdata})

#Creating a json file that contains only the play data

"""
fp = "./play_data/plays.json"
with open(fp, 'w') as fp:
    json.dump(toJson,fp)
"""
