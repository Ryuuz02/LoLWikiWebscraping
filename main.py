from Webscrapers.ChampionNames.ChampionNames import find_names
from Webscrapers.ChampionStats.ChampionStats import return_stats


def check_if_beginning(file):
    with open(file, "a") as file:
        if file.tell() != 0:
            return False
        else:
            return True


if check_if_beginning("Data/ChampNames.txt"):
    names = find_names()
    with open("Data/ChampNames.txt", "w") as f:
        first = True
        for name in names:
            if not first:
                f.write("\n" + name)
            else:
                f.write(name)
                first = False

champion_lst = open("Data/ChampNames.txt", "r").read().split("\n")

champion_stat_lst = []
for champion in champion_lst:
    stat_lst = return_stats(champion)
    stat_lst.insert(0, champion)
    champion_stat_lst.append(stat_lst)
    print("Finished " + champion)

if check_if_beginning("Data/ChampStats.txt"):
    with open("Data/ChampStats.txt", "w") as f:
        for champ_stats in champion_stat_lst:
            f.write(" ".join(champ_stats) + "\n")
