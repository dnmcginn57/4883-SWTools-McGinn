## Data Scraping with beautiful soup
### David McGinn

### Description

This program scrapes live update data from nfl games, and will eventually search for different stats

#### Files:
  * **McGinn_Scraping.py**: this file handles all of the data scraping from the NFL,<br>
                           It gets the gameID's and uses them to generate a url to fetch the json files for each game.<br>
                           stores all of the fetched jsons in a folder called "game_data"
                           
* **Play_Consolidation.py**: Consolidates every play into a single json

* **Stat_Extraction.py**: Responsible for creating and writing stats to stats.txt
