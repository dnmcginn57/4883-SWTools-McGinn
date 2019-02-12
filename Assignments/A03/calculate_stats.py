import os, sys
import json
from pprint import pprint

"""
Make sure the file we're working with is a Json
"""
def isJson(myJson):
    try:
        json_object = json.loads(myJson)
    except ValueError as e:
        return False
    return True

"""
Open plays.json, returns a dictionary
"""
def getFile(path):
    try:
        f = open(path,"r")
        data = f.read()
        if isJson(data):
            return json.loads(data)
        else:
            print("error: not json")
            return {}
    except IOError:
        print("Error: File not found")
        return {}




"""
find player who played for the most teams
accepts a dictionary
returns a sorted list of the top 10 players who played for the most teams
"""
def mostTeams(data):
    #match all players with a list of the teams they've played for
    playernames = {}
    """
    This absolute dumpsterfire of a nested for loop populates
    playernames{} with a list of all teams a player has played for keyed by their name
    """
    for season in data:
        #each play in the season
        for pid in data[season]:
            #each player id that participated in the play
            for player in data[season][pid]['players']:
                #list associated with the player in the play
                for l in data[season][pid]['players'][player]:
                    if l['playerName'] is not None and l['playerName'] != '':
                        #put a player's name in the dictionary, along with the team they are on
                        if l['playerName'] not in playernames:
                            playernames[l['playerName']] = [l['clubcode']]
                        #just add a team to a player if they already exist
                        elif l['clubcode'] not in playernames[l['playerName']]:
                            playernames[l['playerName']].append(l['clubcode'])
    

    #find the player with the longest team list
    Everyone = []
    for player,teams in playernames.items():
        best = (player,len(teams))
        Everyone.append(best)
    
    #sort the list in decending order by number of teams played for
    Everyone.sort(reverse=True, key=lambda elem: elem[1])
    #lop off al but the 10 most traded players
    topTen = Everyone[:10]        

    #return 10 players who have played for the most teams
    return topTen

"""
def teamsOneSeason(data)
accepts a dictionary
Returns a list of players who played for more than one team in a single season
"""
def teamsOneSeason(data):
    pass

"""
def lossRushInfo
called by numRushForLoss() & yrdRushForLoss()
accepts a dictionary
returns a dictionary keyed by player name and a list of their rush stats
"""
def lossRushInfo(data):
    playernames = {}
    rushIDs = [10,12,13]
    """
    """
    for season in data:
        #each play in the season
        for pid in data[season]:
            #each player id that participated in the play
            for player in data[season][pid]['players']:
                #list associated with the player in the play
                for l in data[season][pid]['players'][player]:
                    if l['yards'] is not None and l['yards'] != '':
                        #if the player rushed AND lost yards
                        if int(l['statId']) in rushIDs and int(l['yards']) < 0:
                            if l['playerName'] not in playernames:
                                playernames[l['playerName']] = [l['yards']]
                            else:
                                playernames[l['playerName']].append(int(l['yards']))
    

        
    return playernames

"""
def numRushForLoss()
accepts a dictionary
Returns list of the players who had the most rushes for a loss
"""
def numRushForLoss(data):
    PlayerRushes = lossRushInfo(data)
    lossyPlayers = []
    
    for player, rushes in PlayerRushes.items():
        pTotRush = (player,len(rushes))
        lossyPlayers.append(pTotRush)
    
    lossyPlayers.sort(reverse=True, key=lambda elem: elem[1])
    lossyPlayers = lossyPlayers[:10]

    return lossyPlayers

"""
def yrdRushForLoss()
accepts a dictionary
Returns list of the players who had the most yards rushed for a loss
"""
def yrdRushForLoss(data):
    playerYardRush = lossRushInfo(data)
    lostYards  = []
    for player, yard in playerYardRush.items():
        pYrdLoss = (player, sum(yard))
        lostYards.append(pYrdLoss)
    
    lostYards.sort(key=lambda elem: elem[1])
    lostYards = lostYards[:10]

    return lostYards



playDict = getFile('./play_data/plays.json')
f = open("stats.txt", "w+")
f.write("Name: David McGinn\n")
f.write("Assignment: A03 - NFL Stats\n")
f.write("Date: 2-13-19\n")
f.write("=====================================================\n")

#player who played for the most teams
f.write("1. Find the player that played for the most teams\n\n")
f.write("Answer:\n\n")


pMostTeams = mostTeams(playDict)

for p in pMostTeams:
    f.write(str(p[0]) + " has played for " + str(p[1]) + " teams.\n")

f.write("=====================================================\n")
f.write("2. Find Players that played for multiple teams in a year\n\n")
f.write("Answer:\n\n")

f.write("=====================================================\n")
f.write("3. Find the player that rushed the most yards for a loss\n\n")
f.write("Answer:\n\n")

pMostTeams = yrdRushForLoss(playDict)
for p in pMostTeams:
    f.write(str(p[0]) + " has lost " + str(p[1]) + " yard rushing.\n")

f.write("=====================================================\n")
f.write("4. Find the player that had the most rushes for a loss for a loss\n\n")
f.write("Answer:\n\n")

pMostTeams = numRushForLoss(playDict)
for p in pMostTeams:
    f.write(str(p[0]) + " has rushed for a loss " + str(p[1]) + " times.\n")
    

f.write("=====================================================\n")
f.write("5. Find the player with the most passes for a loss\n\n")
f.write("Answer:\n\n")

f.write("=====================================================\n")
f.write("6. Find the team with the most penalties\n\n")
f.write("Answer:\n\n")

f.write("=====================================================\n")
f.write("7. Find the team with the most yards in penalties\n\n")
f.write("Answer:\n\n")
