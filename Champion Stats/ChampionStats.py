# Import Statements
import requests
from bs4 import BeautifulSoup


# Function to find the attack speed (we need this seperate since it handles a little differently)
def find_attack_speed(stats):
    # Finds the stats we are looking for
    grouped_stats = stats.find_all(class_="pi-item pi-smart-group pi-border-color")
    # index 5 has the base attack speed and attack windup
    base_windup = grouped_stats[5].find_all(class_="pi-smart-data-value pi-data-value pi-font pi-item-spacing "
                                                   "pi-border-color")
    # Takes out the words since we are only looking for numbers
    base_as = base_windup[0].text[7:]
    attack_windup = base_windup[1].text[13:]
    # Index 6 has the as ratio and bonus as
    ratio_bonus = grouped_stats[6].find_all(class_="pi-smart-data-value pi-data-value pi-font pi-item-spacing "
                                                   "pi-border-color")
    # Taking out the words for the numbers, and the percent on the bonus as
    as_ratio = ratio_bonus[0].text[8:]
    bonus_as = ratio_bonus[1].text[9:12]
    # If there is no as ratio, its the same as base as
    if as_ratio == "N/A":
        as_ratio = base_as
    # Returns as list
    return [base_as, attack_windup, as_ratio, bonus_as]


# Function to find the stats of a champion
def find_stats(stats):
    # Creates empty list
    champion_stat_lst = []
    # For each stat we are looking for
    for i in range(0, len(stat_lst)):
        # Gives that stat a variable
        iterated_stat = stat_lst[i]
        # If its a growth stat
        if "Growth" in iterated_stat:
            # Gets rid of the word growth
            iterated_stat = iterated_stat[:-6]
            # Takes it by lvl, and gets rid of the "+" at the beginning
            champion_stat_lst.append(stats.find(id=iterated_stat + "_" + champion + "_lvl").text[1:])
        # Otherwise
        else:
            # Finds that stat
            champion_stat_lst.append(stats.find(id=iterated_stat + "_" + champion).text)
    # Returns the list
    return champion_stat_lst


# Checks the input name, and fixes it if needed
def check_name(name):
    # Kog'Maw is an exception for some reason, and has to specified (No clue why)
    if name == "Kog'Maw":
        return "KogMaw"
    # Creates an empty string
    temp_name = ""
    # For each letter in the name
    for i in range(0, len(name)):
        # If it is the first letter, not an apostrophe or a space
        if name[i] != "'" and i == 0 and name[i] != " ":
            # Adds it capitalized
            temp_name += name[i].upper()
        # If it is not a space or apostrophe
        elif name[i] != "'" and name[i] != " ":
            # If the last letter was a space
            if name[i - 1] == " ":
                # Adds it capitalized
                temp_name += name[i].upper()
            else:
                # Adds it lowercase
                temp_name += name[i].lower()
    # Returns the built name
    return temp_name


# Function that finds main stats, attack speed stats, puts it together, then returns the combined list
def find_all_stats(stats):
    champion_stats = find_stats(stats)
    attack_speed_stats = find_attack_speed(stats)
    combined = champion_stats + attack_speed_stats
    return combined


# Prompts for a champion, finds their corresponding wiki page, and fixes the name if needed
def find_website():
    global champion
    champion = input(
        "What champion would you like to find the stats for? (Note that capitalization and any apostrophes "
        "are necessary for the website to be recognized properly\n")
    url = "https://leagueoflegends.fandom.com/wiki/" + champion + "/LoL"
    website = requests.get(url)
    champion = check_name(champion)
    return website


# Prints out each stat name and the associated value
def print_stats(stats):
    for i in range(0, len(combined_stats)):
        print(combined_stat_lst[i] + " " + stats[i])


# Finds the exact stat container we are looking for and returns it
def find_stat_info(website):
    parsed = BeautifulSoup(website.content, "html.parser")
    infographic = parsed.find_all(class_="portable-infobox")
    stat_info = infographic[3]
    return stat_info


champion = ""
# All the stats we can find
stat_lst = ["Health", "HealthGrowth", "ResourceBar", "ResourceBarGrowth", "HealthRegen", "HealthRegenGrowth",
            "ResourceRegen", "ResourceRegenGrowth", "Armor", "ArmorGrowth", "AttackDamage", "AttackDamageGrowth",
            "MagicResist", "MagicResistGrowth", "MovementSpeed", "AttackRange"]
# Attack speed stats
attack_stat_lst = ["Base AS", "Attack Windup", "AS Ratio", "Bonus AS"]
combined_stat_lst = stat_lst + attack_stat_lst
# Does all the searching
combined_stats = find_all_stats(find_stat_info(find_website()))
# Then prints the stats
print_stats(combined_stats)
