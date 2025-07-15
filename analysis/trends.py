import pandas as pd

def add_trend_features(matches, puuid):
    rows = []
    for match in matches:
        player = next(p for p in match["info"]["participants"] if p["puuid"] == puuid)
        game_duration_min = match["info"]["gameDuration"] / 60

        rows.append({
            "timestamp": pd.to_datetime(match["info"]["gameStartTimestamp"], unit='ms'),
            "champion": player["championName"],
            "kills": player["kills"],
            "deaths": player["deaths"],
            "assists": player["assists"],
            "cs": player["totalMinionsKilled"] + player["neutralMinionsKilled"],
            "win": player["win"],
            "duration": game_duration_min
        })

    df = pd.DataFrame(rows)
    df["KDA"] = (df["kills"] + df["assists"]) / df["deaths"].replace(0, 1)
    df["CS_per_min"] = df["cs"] / df["duration"]
    df.sort_values("timestamp", inplace=True)
    return df.reset_index(drop=True)
