
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

finals = pd.read_csv("refined_finals_data.csv")

finals.replace(1610612738,"Boston Celtics",inplace=True)
finals.replace(1610612742 ,"Dallas mavericks",inplace=True)
finals.replace(1610612743 ,"Denver Nuggets",inplace=True)
finals.replace(1610612748 ,"Miami Heat",inplace=True)
finals.replace(1610612744 ,"Golden State Warriors",inplace=True)
finals.replace(1610612749 ,"Milwaukee Bucks",inplace=True)
finals.replace(1610612756 ,"Phoenix Suns",inplace=True)
finals.replace(1610612747 ,"Los Angeles Lakers",inplace=True)


finals["Point Differential"] = (finals["Avg_Points_Scored"]-finals["Avg_Points_Allowed"])

sns.scatterplot(data=finals,x="Team_ID",y="Point Differential",hue="Season")
plt.show()

