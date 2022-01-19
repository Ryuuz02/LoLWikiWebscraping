# Import Statements
import requests
from bs4 import BeautifulSoup


def find_attack_speed(stats):
    grouped_stats = stats.find_all(class_="pi-item pi-smart-group pi-border-color")
    base_windup = grouped_stats[5].find_all(class_="pi-smart-data-value pi-data-value pi-font pi-item-spacing "
                                                   "pi-border-color")
    base_as = base_windup[0].text[7:]
    attack_windup = base_windup[1].text[13:]
    ratio_bonus = grouped_stats[6].find_all(class_="pi-smart-data-value pi-data-value pi-font pi-item-spacing "
                                                   "pi-border-color")
    as_ratio = ratio_bonus[0].text[8:]
    bonus_as = ratio_bonus[1].text[9:12]
    if as_ratio == "N/A":
        as_ratio = base_as
    return [base_as, attack_windup, as_ratio, bonus_as]


def find_stats(stats):
    champion_stat_lst = []
    for i in range(0, len(stat_lst)):
        iterated_stat = stat_lst[i]
        if "Growth" in iterated_stat:
            iterated_stat = iterated_stat[:-6]
            champion_stat_lst.append(stats.find(id=iterated_stat + "_" + champion + "_lvl").text[1:])
        else:
            champion_stat_lst.append(stats.find(id=iterated_stat + "_" + champion).text)
    return champion_stat_lst


def check_name(name):
    if name == "Kog'Maw":
        return "KogMaw"
    temp_name = ""
    for i in range(0, len(name)):
        if name[i] != "'" and i == 0 and name[i] != " ":
            temp_name += name[i].upper()
        elif name[i] != "'" and name[i] != " ":
            if name[i - 1] == " ":
                temp_name += name[i].upper()
            else:
                temp_name += name[i].lower()
    return temp_name


def find_all_stats(stats):
    champion_stats = find_stats(stats)
    attack_speed_stats = find_attack_speed(stats)
    combined = champion_stats + attack_speed_stats
    return combined


def find_website():
    global champion
    champion = input(
        "What champion would you like to find the stats for? (Note that capitalization and any apostrophes "
        "are necessary for the website to be recognized properly\n")
    url = "https://leagueoflegends.fandom.com/wiki/" + champion + "/LoL"
    website = requests.get(url)
    champion = check_name(champion)
    return website


def print_stats(stats):
    for i in range(0, len(combined_stats)):
        print(combined_stat_lst[i] + " " + stats[i])


def find_stat_info(website):
    parsed = BeautifulSoup(website.content, "html.parser")
    infographic = parsed.find_all(class_="portable-infobox")
    stat_info = infographic[3]
    return stat_info


champion = ""
stat_lst = ["Health", "HealthGrowth", "ResourceBar", "ResourceBarGrowth", "HealthRegen", "HealthRegenGrowth",
            "ResourceRegen", "ResourceRegenGrowth", "Armor", "ArmorGrowth", "AttackDamage", "AttackDamageGrowth",
            "MagicResist", "MagicResistGrowth", "MovementSpeed", "AttackRange"]
attack_stat_lst = ["Base AS", "Attack Windup", "AS Ratio", "Bonus AS"]
combined_stat_lst = stat_lst + attack_stat_lst


combined_stats = find_all_stats(find_stat_info(find_website()))
print_stats(combined_stats)
