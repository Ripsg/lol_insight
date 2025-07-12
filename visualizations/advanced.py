import matplotlib.pyplot as plt

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
