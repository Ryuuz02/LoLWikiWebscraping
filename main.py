from Webscrapers.ChampionNames.ChampionNames import find_names
from Webscrapers.ChampionStats.ChampionStats import return_stats

champion_lst = find_names()
champion_stat_lst = []
for i in range(0, len(champion_lst)):
    stat_lst = return_stats(champion_lst[i])
    stat_lst.insert(0, champion_lst[i])
    champion_stat_lst.append(stat_lst)
print(champion_stat_lst)
