import pandas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

lakers_finals_player_2020 = pd.read_csv("lakers2020finals.csv", nrows=1)
heat_finals_player_2020 = pd.read_csv("heat2020finals.csv", nrows=1)
bucks_finals_player_2021 = pd.read_csv("bucks2021finals.csv", nrows=1)
suns_finals_player_2021 = pd.read_csv("suns2021finals.csv", nrows=1)
warriors_finals_player_2022 = pd.read_csv("warriors2022finals.csv", nrows=1)
celtics_finals_player_2022 = pd.read_csv("celtics2022finals.csv", nrows=1)
nuggets_finals_player_2023 = pd.read_csv("nuggets2023finals.csv", nrows=1)
heat_finals_player_2023 = pd.read_csv("heat2023finals.csv", nrows=1)
celtics_finals_player_2024 = pd.read_csv("celtics2022finals.csv", nrows=1)
mavs_finals_player_2024 = pd.read_csv("mavs2024finals.csv", nrows=1)

combined_finals_player = pandas.concat([lakers_finals_player_2020,
                                             heat_finals_player_2020])
combined_finals_player_2021 = pandas.concat([bucks_finals_player_2021,
                                           suns_finals_player_2021])
combined_finals_player = pandas.concat([combined_finals_player,
                                             combined_finals_player_2021])
combined_finals_player_2022 = pandas.concat([warriors_finals_player_2022,
                                           celtics_finals_player_2022])
combined_finals_player = pandas.concat([combined_finals_player,
                                             combined_finals_player_2022])
combined_finals_player_2023 = pandas.concat([nuggets_finals_player_2023,
                                           heat_finals_player_2023])
combined_finals_player = pandas.concat([combined_finals_player,
                                             combined_finals_player_2023])
combined_finals_player_2024 = pandas.concat([celtics_finals_player_2024,
                                           mavs_finals_player_2024])
combined_finals_player = pandas.concat([combined_finals_player,
                                             combined_finals_player_2024])

combined_finals_player.iloc[0,combined_finals_player.columns.get_loc('Rk')]=2020
combined_finals_player.iloc[1,combined_finals_player.columns.get_loc('Rk')]=2020
combined_finals_player.iloc[2,combined_finals_player.columns.get_loc('Rk')]=2021
combined_finals_player.iloc[3,combined_finals_player.columns.get_loc('Rk')]=2021
combined_finals_player.iloc[4,combined_finals_player.columns.get_loc('Rk')]=2022
combined_finals_player.iloc[5,combined_finals_player.columns.get_loc('Rk')]=2022
combined_finals_player.iloc[6,combined_finals_player.columns.get_loc('Rk')]=2023
combined_finals_player.iloc[7,combined_finals_player.columns.get_loc('Rk')]=2023
combined_finals_player.iloc[8,combined_finals_player.columns.get_loc('Rk')]=2024
combined_finals_player.iloc[9,combined_finals_player.columns.get_loc('Rk')]=2024


combined_finals_player.rename(columns={"Rk": "Year"}, inplace=True)

sns.catplot(data=combined_finals_player, kind = "bar",
            x="Year", y="GmSc", hue = "Player")
plt.show()


