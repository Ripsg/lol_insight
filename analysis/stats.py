import pandas as pd

def extract_basic_stats(matches, puuid):
    stats = []
    for match in matches:
        player_data = next(p for p in match['info']['participants'] if p['puuid'] == puuid)
        stats.append({
            "champion": player_data["championName"],
            "kills": player_data["kills"],
            "deaths": player_data["deaths"],
            "assists": player_data["assists"],
            "win": player_data["win"]
        })
    return pd.DataFrame(stats)
