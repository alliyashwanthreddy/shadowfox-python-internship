import pandas as pd
import matplotlib.pyplot as plt

# Load fielding dataset
df = pd.read_excel("IPL_sample_data.xlsx")

# Select three players
players = df["Player"].unique()[:3]

player_data = df[df["Player"].isin(players)]

# Calculate performance metrics
summary = player_data.groupby("Player").agg({
    "BallCount": "count",
    "Runs": "sum",
    "Pick": lambda x: (x == "Y").sum(),
    "Throw": lambda x: (x == "Y").sum()
})

summary.columns = [
    "Fielding Chances",
    "Runs Saved",
    "Successful Picks",
    "Successful Throws"
]

summary["Pick Success %"] = (
    summary["Successful Picks"] /
    summary["Fielding Chances"] * 100
).round(2)

summary["Throw Success %"] = (
    summary["Successful Throws"] /
    summary["Fielding Chances"] * 100
).round(2)

print("\nFIELDING PERFORMANCE REPORT\n")
print(summary)

# Save report
summary.to_excel("Fielding_Performance_Report.xlsx")

# Visualization
summary["Runs Saved"].plot(
    kind="bar",
    figsize=(8,5),
    title="Runs Saved by Players"
)

plt.ylabel("Runs Saved")
plt.tight_layout()
plt.show()

print("\nReport saved successfully.")