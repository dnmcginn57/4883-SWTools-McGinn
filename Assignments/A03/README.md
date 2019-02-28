## Data Scraping with beautiful soup
### David McGinn

### Description

This program scrapes live update data from nfl games, and will eventually search for different stats

#### Files:
  * **McGinn_Scraping.py**: this file handles all of the data scraping from the NFL,<br>
                           It gets the gameID's and uses them to generate a url to fetch the json files for each game.<br>
                           stores all of the fetched jsons in a folder called "game_data"
                           
* **Play_Consolidation.py**: Consolidates every play into a single json

* **calculate_stats.py**: Responsible for creating and writing stats to stats.txt

#### Instructions:
1. create folders `game_data` and `play_data` in the same directory as the other files
2. run `McGinn_Scraping.py` to scrape all of the liveupdate game jsons into `game_data`
3. run `Play_Consolidation.py` to create a json that stores all plays by season
4. run `calculate_stats.py` this should create a text file called `stats.txt` which contains the output for the program
