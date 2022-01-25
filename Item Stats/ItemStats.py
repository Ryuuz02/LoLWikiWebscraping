# Import Statements
import urllib.request

import requests
from bs4 import BeautifulSoup
from urllib import request


# Function to find a website and return its parsed data
def find_and_parse():
    # Url for immortal shieldbow (Will be changed to work for any item in the future
    url = "https://leagueoflegends.fandom.com/wiki/Immortal_Shieldbow"
    # Gets the website, then parses it with the html parser to clean it up
    website = requests.get(url)
    parsed_version = BeautifulSoup(website.content, "html.parser")
    return parsed_version


# Function to find the containers for each part of the info we are looking for
def find_infoboxes(parsed_data):
    # Gets the info box on the page with all the information
    itembox = parsed_data.find(class_="portable-infobox pi-background pi-border-color pi-theme-wikia pi-layout-stacked")
    # Finds the box that has all the stats we are looking for
    seperated_boxes = itembox.find_all(class_="pi-item pi-group pi-border-color")
    return seperated_boxes[0], seperated_boxes[1], seperated_boxes[2], seperated_boxes[5]


# finds the infobox that has the stats we are looking for and returns it
def find_stats():
    # Finds each stat, but this still includes the formatting and extra html information
    stat_and_formatting = statbox.find_all(class_="pi-item pi-data pi-item-spacing pi-border-color")
    # Creates an empty list
    stats_only = []
    # For each stat
    for stat in range(0, len(stat_and_formatting)):
        # Appends its stats information to the stats only
        stats_only.append(stat_and_formatting[stat].find(class_="pi-data-value pi-font"))
    return stats_only


# Takes in the html info and converts it to a string list, then returns that list
def stat_info_to_string_lst(stats):
    # Creates an empty list
    lst_stats = []
    # For each stat
    for i in range(0, len(stats)):
        # Takes the text (The actual stats and info) and splits it by word
        split_version = stats[i].text[1:].split(" ")
        # Then adds it to the split stats, if there is a parenthesis, takes it out (will make later processes easier)
        if "%" in split_version[0]:
            split_version[0] = split_version[0][0:len(split_version[0]) - 1]
        lst_stats.append(split_version)
    return lst_stats


# Checks if the item has the right wording to indicate a mythic item
def is_mythic(passives):
    # For each passive
    for passive in passives:
        # Checks if has a mythic passive
        if "Mythic Passive:" in passive:
            return True
    return False


# Finds every passive in the infobox and adds it to a list that is then returned
def find_and_list_passives(infobox):
    passives_and_formatting = infobox.find_all(class_="pi-item pi-data pi-item-spacing pi-border-color")
    passives = []
    for passive in range(0, len(passives_and_formatting)):
        passives.append(passives_and_formatting[passive].find(class_="pi-data-value pi-font").text)
    return passives


# Finds the website, parses it, and finds the appropriate boxes of info
parsed = find_and_parse()
picbox, statbox, abilitybox, costbox = find_infoboxes(parsed)

cost_info = costbox.find("tbody")
total_cost = cost_info.find(style="white-space:normal").text
print(total_cost)


picture = picbox.find("img", alt="Immortal Shieldbow")
urllib.request.urlretrieve(picture["src"], "C:\\Users\\Jacob Bode\\PycharmProjects\\LoLWikiWebscraping\\test.jpg")

# Finds the stats and puts it into a list
stat_info = find_stats()
split_stats = stat_info_to_string_lst(stat_info)
# print(split_stats)

# Finds the passives and puts it into a list
item_passives = find_and_list_passives(abilitybox)
# print(*item_passives, sep="\n")
# print(is_mythic(item_passives))
