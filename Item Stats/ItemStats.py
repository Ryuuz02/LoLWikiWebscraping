# Import Statements
import requests
from bs4 import BeautifulSoup

# Url for immortal shieldbow (Will be changed to work for any item in the future
url = "https://leagueoflegends.fandom.com/wiki/Immortal_Shieldbow"
# Gets the website, then parses it with the html parser to clean it up
website = requests.get(url)
parsed = BeautifulSoup(website.content, "html.parser")
# Gets the info box on the page with all the information
itembox = parsed.find(class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-stacked")
# Finds the box that has all the stats we are looking for
statbox = itembox.find_all(class_="pi-item pi-group pi-border-color")[1]
# Finds each stat, but this still includes the formatting and extra html information
stat_and_formatting = statbox.find_all(class_="pi-item pi-data pi-item-spacing pi-border-color")
# Creates an empty list
stats_only = []
# For each stat
for i in range(0, len(stat_and_formatting)):
    # Appends its stats information to the stats only
    stats_only.append(stat_and_formatting[i].find(class_="pi-data-value pi-font"))
# Creates an empty list
split_stats = []
# For each stat
for i in range(0, len(stats_only)):
    # Takes the text (The actual stats and info) and splits it by word
    split_version = stats_only[i].text[1:].split(" ")
    # Then adds it to the split stats, if there is a parenthesis, takes it out (will make later processes easier)
    if "%" in split_version[0]:
        split_version[0] = split_version[0][0:len(split_version[0]) - 1]
    split_stats.append(split_version)
print(split_stats)
