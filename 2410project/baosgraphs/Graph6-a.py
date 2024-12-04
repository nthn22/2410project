import pandas as pd
import matplotlib.pyplot as plt

# Load the data (replace with your actual file path if necessary)
file_path = 'Combined_Finals_Four_Factors.csv'
data = pd.read_csv(file_path)

# Specify the columns you want to use
columns_to_use = ["Category", "2022_23_DEN", "2022_23_MIA"]
subset_data = data[columns_to_use]

# Transpose the data for easier plotting (Categories become columns, Teams/Years become rows)
subset_data = subset_data.set_index("Category").T

# Rescale eFG% and FT/FGA for better visualization
subset_data_rescaled = subset_data.copy()
subset_data_rescaled.loc[:, "eFG%"] = subset_data["eFG%"] * 100  # Scale to percentage
subset_data_rescaled.loc[:, "FT/FGA"] = subset_data["FT/FGA"] * 100  # Scale to percentage

# Prepare data for plotting
categories = subset_data_rescaled.columns
teams_years = subset_data_rescaled.index
x = range(len(teams_years))  # X positions for the teams/years
width = 0.12  # Smaller bar width for better spacing

# Plot the bar chart
plt.figure(figsize=(10, 6))

# Plot bars for each category with appropriate spacing
for i, category in enumerate(categories):
    plt.bar(
        [pos + i * width for pos in x],  # Offset each category
        subset_data_rescaled[category],
        width=width,
        label=category
    )

# Add labels, title, and legend
plt.xticks([pos + (width * (len(categories) - 1) / 2) for pos in x], teams_years, rotation=45)
plt.xlabel("Team/Year")
plt.ylabel("Value (Scaled for eFG% and FT/FGA)")
plt.title("Key Basketball Metrics for the 2022-23 Season")
plt.legend()
plt.tight_layout()
plt.show()
