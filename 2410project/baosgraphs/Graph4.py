import pandas as pd
import matplotlib.pyplot as plt

#loads dataset
file_path = 'NBA Finals and MVP.csv'
data = pd.read_csv(file_path)

#calculates number of championships won by each team
championship_counts = data['NBA Champion'].value_counts()

#plotting the bar chart
plt.figure(figsize=(12, 6))
championship_counts.plot(kind='bar', edgecolor='black')
plt.title('Number of Championships by Team')
plt.xlabel('Teams')
plt.ylabel('Number of Championships')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
