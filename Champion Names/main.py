from bs4 import BeautifulSoup
import requests

url = "https://www.leagueoflegends.com/en-us/champions/"
website = requests.get(url)
parsed = BeautifulSoup(website.content, "html.parser")
champion_table = parsed.find("div", class_="style__List-sc-13btjky-2 dLJiol")
champions = champion_table.find_all("span", class_="style__Text-n3ovyt-3 gMLOLF")
for i in range(0, len(champions)):
    print(champions[i].text)
