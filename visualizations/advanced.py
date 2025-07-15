import matplotlib.pyplot as plt
import seaborn as sns

def plot_kda_timeline(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["KDA"], marker="o", label="KDA")
    plt.title("KDA Over Time")
    plt.xlabel("Match Date")
    plt.ylabel("KDA")
    plt.grid()
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_cs_trend(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["timestamp"], df["CS_per_min"], marker="x", color="orange", label="CS/min")
    plt.title("CS per Minute Over Time")
    plt.xlabel("Match Date")
    plt.ylabel("CS/min")
    plt.grid()
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def plot_champion_heatmap(df):
    grouped = df.groupby("champion").agg({
        "KDA": "mean",
        "CS_per_min": "mean",
        "win": "mean"
    }).rename(columns={"win": "Win Rate"})

    plt.figure(figsize=(8, 6))
    sns.heatmap(grouped, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Champion Performance Heatmap")
    plt.tight_layout()
    plt.show()

def plot_playstyles(df):
    style_counts = df["playstyle"].value_counts()
    style_counts.plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Playstyle Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

