import matplotlib as plt

def classify_playstyle(df):
    styles = []
    for _, row in df.iterrows():
        score = (row["kills"], row["assists"], row["KDA"])

        if row["kills"] >= 10:
            styles.append("Aggressive")
        elif row["assists"] >= 10 and row["kills"] < 4:
            styles.append("Supportive")
        elif row["KDA"] < 1.5:
            styles.append("Passive")
        else:
            styles.append("Balanced")

    df["playstyle"] = styles
    return df

def plot_playstyles(df):
    style_counts = df["playstyle"].value_counts()
    style_counts.plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Playstyle Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
