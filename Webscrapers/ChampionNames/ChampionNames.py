from bs4 import BeautifulSoup
import requests


def find_website():
    url = "https://www.leagueoflegends.com/en-us/champions/"
    website = requests.get(url)
    parsed = BeautifulSoup(website.content, "html.parser")
    return parsed


def find_names():
    parsed = find_website()
    champion_table = parsed.find("div", class_="style__List-sc-13btjky-2 dLJiol")
    champions = champion_table.find_all("span", class_="style__Text-n3ovyt-3 gMLOLF")
    champion_lst = []
    for i in range(0, len(champions)):
        champion_lst.append(champions[i].text)
    return champion_lst
