import matplotlib.pyplot as plt

def plot_kda(df):
    df['KDA'] = (df['kills'] + df['assists']) / df['deaths'].replace(0, 1)
    df.plot(y='KDA', kind='line', marker='o', title="KDA Over Matches")
    plt.show()

def plot_win_rate(df):
    champ_win = df.groupby('champion')['win'].mean() * 100
    champ_win.sort_values().plot(kind='barh', title="Win Rate by Champion")
    plt.xlabel("Win %")
    plt.show()

def plot_playstyles(df):
    style_counts = df["playstyle"].value_counts()
    style_counts.plot.pie(autopct="%1.1f%%", startangle=90)
    plt.title("Playstyle Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()
