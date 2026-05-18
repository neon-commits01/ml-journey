import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")


# Most wins
most_wins = matches["winner"].value_counts().idxmax()
# Most runs
most_runs = deliveries.groupby("batsman")["total_runs"].sum().idxmax()
# Most wickets
wickets = deliveries[(deliveries["dismissal_kind"].notna()) & (deliveries["dismissal_kind"] != "run out")]
most_wickets = wickets.groupby("bowler")["dismissal_kind"].count().idxmax()
# Top Venue
top_venue = matches["venue"].value_counts().idxmax()

# Season with Highest avg score
runs_per_match = deliveries.groupby("match_id")["total_runs"].sum().reset_index()
runs_per_match = runs_per_match.rename(columns={"match_id": "id"})
merged = pd.merge(runs_per_match, matches[["id", "season"]], on="id")
avg_score_per_season = merged.groupby("season")["total_runs"].mean()


# Visualize using Bar and Line charts
top_venue_chart = matches["venue"].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.bar(top_venue_chart.index, top_venue_chart.values, color="steelblue")
plt.title("Top 10 Match Venues in IPL")
plt.xlabel("Venue")
plt.ylabel("Number of matches")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

avg_score_per_season = merged.groupby("season")["total_runs"].mean()
plt.figure(figsize=(10,6))
plt.plot(avg_score_per_season.index, avg_score_per_season.values, marker="o", color="orange")
plt.title("Average Match Score By IPL Season")
plt.xlabel("Season")
plt.ylabel("Total Runs")
plt.tight_layout()
plt.show()