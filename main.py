from riot_api.account import get_account_by_riot_id
from riot_api.match import get_match_ids, get_match_data
from analysis.stats import extract_basic_stats
from visualizations.plots import plot_kda, plot_win_rate
from analysis.trends import add_trend_features
from analysis.profiling import classify_playstyle
from analysis.recommendation import recommend_champions
from visualizations.advanced import plot_kda_timeline, plot_cs_trend, plot_champion_heatmap, plot_playstyles
from utils.regions import REGION_MAP
import json, os

def main():
    print("📊 Welcome to LoL Insight Tracker")
    riot_id = input("Enter your Riot ID (GameName#TagLine): ").strip()
    region_input = input("Enter region (e.g. NA, EUW, LAN): ").strip().upper()

    if region_input not in REGION_MAP:
        print(f"❌ Region '{region_input}' is not supported.")
        return

    platform, routing = REGION_MAP[region_input]

    try:
        game_name, tag_line = riot_id.split("#")
    except ValueError:
        print("❌ Invalid Riot ID format. Use GameName#TagLine.")
        return

    print(f"🔍 Fetching account for {game_name}#{tag_line} in {region_input}...")

    account = get_account_by_riot_id(game_name, tag_line, routing)
    puuid = account["puuid"]

    match_ids = get_match_ids(puuid, routing, count=10)
    matches = [get_match_data(mid, routing) for mid in match_ids]

    os.makedirs("data", exist_ok=True)
    with open(f"data/{game_name}_{tag_line}_{region_input}_matches.json", "w") as f:
        json.dump(matches, f, indent=2)

    df = extract_basic_stats(matches, puuid)
    print(df.head())

    plot_kda(df)
    plot_win_rate(df)

    def run_intermediate_analysis(matches, puuid):
        df = add_trend_features(matches, puuid)
        df = classify_playstyle(df)

        plot_kda_timeline(df)
        plot_cs_trend(df)
        plot_champion_heatmap(df)
        plot_playstyles(df)

        print("🎯 Recommended Champions:")
        print(recommend_champions(df))
    run_intermediate_analysis(matches, puuid)


if __name__ == "__main__":
    main()
    
