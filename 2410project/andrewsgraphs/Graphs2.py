import pandas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


western_conference_2020 = pd.read_csv("NBA_2020_Western_Conference_Standings.csv")
western_conference_2020.rename(columns={"Western Conference": "Team"}, inplace=True)
western_conference_2020["Conference"] = 2020
western_conference_2020.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
western_conference_2021 = pd.read_csv("NBA_2021_Western_Conference_Standings.csv")
western_conference_2021.rename(columns={"Western Conference":"Team"}, inplace=True)
western_conference_2021["Conference"] = 2021
western_conference_2021.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
western_conference_2022 = pd.read_csv("NBA_2022_Western_Conference_Standings.csv")
western_conference_2022.rename(columns={"Western Conference":"Team"},inplace=True)
western_conference_2022["Conference"] = 2022
western_conference_2022.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
western_conference_2023 = pd.read_csv("NBA_2023_Western_Conference_Standings.csv")
western_conference_2023.rename(columns={"Western Conference":"Team"},inplace=True)
western_conference_2023["Conference"] = 2023
western_conference_2023.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
western_conference_2024 = pd.read_csv("NBA_2024_Western_Conference_Standing.csv")
western_conference_2024.rename(columns={"Western Conference":"Team"})
western_conference_2024.drop(["W","L","SOS","rSOS","SRS","Current","Remain",
                              "Best","Worst","Playoffs","Division","1","2","3","4","5",
                              "6","7","8","1-6","7","8","9","10","Out","Win Conf",
                              "Win Finals"],
                             axis=1 , inplace=True)
western_conference_2024 = western_conference_2024.loc[:,:"W/L%"]
western_conference_2024["Conference"] = 2024


eastern_conference_2020 = pd.read_csv("NBA_2020_Eastern_Conference_Standings.csv")
eastern_conference_2020.rename(columns={"Eastern Conference":"Team"},inplace=True)
eastern_conference_2020["Conference"] = 2020
eastern_conference_2020.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
eastern_conference_2021 = pd.read_csv("NBA_2021_Eastern_Conference_Standings.csv")
eastern_conference_2021.rename(columns={"Eastern Conference":"Team"},inplace=True)
eastern_conference_2021["Conference"] = 2021
eastern_conference_2021.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
eastern_conference_2022 = pd.read_csv("NBA_2022_Eastern_Conference_Standings.csv")
eastern_conference_2022.rename(columns={"Eastern Conference":"Team"},inplace=True)
eastern_conference_2022["Conference"] = 2022
eastern_conference_2022.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
eastern_conference_2023 = pd.read_csv("NBA_2023_Eastern_Conference_Standings.csv")
eastern_conference_2023.rename(columns={"Eastern Conference":"Team"},inplace=True)
eastern_conference_2023["Conference"] = 2023
eastern_conference_2023.drop(["W","L","GB","PS/G","PA/G","SRS"],
                             axis=1 , inplace=True)
eastern_conference_2024 = pd.read_csv("NBA_2024_Eastern_Conference_Standing.csv")
eastern_conference_2024.rename(columns={"Eastern Conference":"Team"},inplace=True)
eastern_conference_2024.drop(["W","L","SOS","rSOS","SRS","Current","Remain",
                              "Best","Worst","Playoffs","Division","1","2","3","4","5",
                              "6","7","8","1-6","7","8","9","10","Out","Win Conf",
                              "Win Finals"],
                             axis=1 , inplace=True)
eastern_conference_2024 = eastern_conference_2024.loc[:,:"W/L%"]
eastern_conference_2024["Conference"] = 2024

combined_conferences = pandas.concat([western_conference_2020,
                                             eastern_conference_2020])
combined_conferences_2021 = pandas.concat([western_conference_2021,
                                           eastern_conference_2021])
combined_conferences = pandas.concat([combined_conferences,
                                             combined_conferences_2021])
combined_conferences_2022 = pandas.concat([western_conference_2022,
                                           eastern_conference_2022])
combined_conferences = pandas.concat([combined_conferences,
                                             combined_conferences_2022])
combined_conferences_2023 = pandas.concat([western_conference_2023,
                                           eastern_conference_2023])
combined_conferences = pandas.concat([combined_conferences,
                                             combined_conferences_2023])
combined_conferences_2024= pandas.concat([western_conference_2024,
                                           eastern_conference_2024])
combined_conferences = pandas.concat([combined_conferences,
                                             combined_conferences_2024])
combined_conferences.rename(columns={"Conference": "Year"}, inplace=True)


sns.scatterplot(data=combined_conferences, x = "Year", y = "W/L%",
                hue = "Team")
plt.xticks([2020, 2021, 2022, 2023, 2024])
legend = plt.gca().get_legend()

legend.set_visible(not legend.get_visible())

plt.show()