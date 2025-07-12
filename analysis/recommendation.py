def recommend_champions(df, min_games=2):
    grouped = df.groupby("champion").agg({
        "KDA": "mean",
        "win": ["mean", "count"]
    })
    grouped.columns = ["KDA", "Win Rate", "Games"]
    filtered = grouped[grouped["Games"] >= min_games]
    recommended = filtered.sort_values(by=["Win Rate", "KDA"], ascending=False)
    return recommended.head(5)
