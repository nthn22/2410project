import pandas
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

lakers_points_2020 = pd.read_csv("lakers_home_record_with_point_differentials_2019_2020.csv")
lakers_points_2020.rename(columns={"GAME_DATE": "Year"}, inplace=True)
lakers_points_2020["Year"] = 2020
lakers_points_2020.rename(columns={"MATCHUP": "Team"}, inplace=True)
lakers_points_2020["Team"] = "Lakers"
lakers_points_2020.drop(["PTS"],
                             axis=1 , inplace=True)

heat_points_2020 = pd.read_csv("heat_home_record_with_point_differentials_2019_2020.csv")
heat_points_2020.rename(columns={"GAME_DATE": "Year"}, inplace=True)
heat_points_2020["Year"] = 2020
heat_points_2020.rename(columns={"MATCHUP": "Team"}, inplace=True)
heat_points_2020["Team"] = "Heat"
heat_points_2020.drop(["PTS"],
                             axis=1 , inplace=True)

bucks_points_2021 = pd.read_csv("bucks_home_record_with_point_differentials_2020_2021.csv")
bucks_points_2021.rename(columns={"GAME_DATE": "Year"}, inplace=True)
bucks_points_2021["Year"] = 2021
bucks_points_2021.rename(columns={"MATCHUP": "Team"}, inplace=True)
bucks_points_2021["Team"] = "Bucks"
bucks_points_2021.drop(["PTS"],
                             axis=1 , inplace=True)

suns_points_2021 = pd.read_csv("bucks_home_record_with_point_differentials_2020_2021.csv")
suns_points_2021.rename(columns={"GAME_DATE": "Year"}, inplace=True)
suns_points_2021["Year"] = 2021
suns_points_2021.rename(columns={"MATCHUP": "Team"}, inplace=True)
suns_points_2021["Team"] = "Suns"
suns_points_2021.drop(["PTS"],
                             axis=1 , inplace=True)

warriors_points_2022 = pd.read_csv("warriors_home_record_with_point_differentials_2021_2022.csv")
warriors_points_2022.rename(columns={"GAME_DATE": "Year"}, inplace=True)
warriors_points_2022["Year"] = 2022
warriors_points_2022.rename(columns={"MATCHUP": "Team"}, inplace=True)
warriors_points_2022["Team"] = "Warriors"
warriors_points_2022.drop(["PTS"],
                             axis=1 , inplace=True)

celtics_points_2022 = pd.read_csv("celtics_home_record_with_point_differentials_2021_2022.csv")
celtics_points_2022.rename(columns={"GAME_DATE": "Year"}, inplace=True)
celtics_points_2022["Year"] = 2022
celtics_points_2022.rename(columns={"MATCHUP": "Team"}, inplace=True)
celtics_points_2022["Team"] = "Celtics"
celtics_points_2022.drop(["PTS"],
                             axis=1 , inplace=True)

nuggets_points_2023 = pd.read_csv("denver_nuggets_home_record_with_point_differentials_2022_2023.csv")
nuggets_points_2023.rename(columns={"GAME_DATE": "Year"}, inplace=True)
nuggets_points_2023["Year"] = 2023
nuggets_points_2023.rename(columns={"MATCHUP": "Team"}, inplace=True)
nuggets_points_2023["Team"] = "Nuggets"
nuggets_points_2023.drop(["PTS"],
                             axis=1 , inplace=True)

heat_points_2023 = pd.read_csv("denver_nuggets_home_record_with_point_differentials_2022_2023.csv")
heat_points_2023.rename(columns={"GAME_DATE": "Year"}, inplace=True)
heat_points_2023["Year"] = 2023
heat_points_2023.rename(columns={"MATCHUP": "Team"}, inplace=True)
heat_points_2023["Team"] = "Heat"
heat_points_2023.drop(["PTS"],
                             axis=1 , inplace=True)


celtics_points_2024 = pd.read_csv("boston_celtics_home_record_with_point_differentials_2023_2024.csv")
celtics_points_2024.rename(columns={"GAME_DATE": "Year"}, inplace=True)
celtics_points_2024["Year"] = 2024
celtics_points_2024.rename(columns={"MATCHUP": "Team"}, inplace=True)
celtics_points_2024["Team"] = "Celtics"
celtics_points_2024.drop(["PTS"],
                             axis=1 , inplace=True)


mavs_points_2024 = pd.read_csv("dallas_mavericks_home_record_with_point_differentials_2023_2024.csv")
mavs_points_2024.rename(columns={"GAME_DATE": "Year"}, inplace=True)
mavs_points_2024["Year"] = 2024
mavs_points_2024.rename(columns={"MATCHUP": "Team"}, inplace=True)
mavs_points_2024["Team"] = "Mavs"
mavs_points_2024.drop(["PTS"],
                             axis=1 , inplace=True)

combined_points = pandas.concat([lakers_points_2020,heat_points_2020])
points_2021 = pandas.concat([bucks_points_2021,suns_points_2021])
combined_points = pandas.concat([combined_points,points_2021])
points_2022 = pandas.concat([warriors_points_2022,celtics_points_2022])
combined_points = pandas.concat([combined_points,points_2022])
points_2023 = pandas.concat([nuggets_points_2023,heat_points_2023])
combined_points = pandas.concat([combined_points,points_2023])
points_2024 = pandas.concat([celtics_points_2024,mavs_points_2024])
combined_points = pandas.concat([combined_points,points_2024])


sns.catplot(data=combined_points, kind = "bar",
            x="Year", y="POINT_DIFFERENTIAL", hue="Team", errorbar=None)
plt.show()