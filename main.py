import os
import json
import asyncio
from dotenv import load_dotenv

# Internal imports
from riot_api.account import get_account_by_riot_id
from riot_api.match import get_match_ids, fetch_all_matches  # ✅ Fix: added get_match_ids
from analysis.stats import extract_basic_stats
from analysis.trends import add_trend_features
from analysis.profiling import classify_playstyle
from analysis.recommendation import recommend_champions
from visualizations.plots import plot_kda, plot_win_rate
from visualizations.advanced import (
    plot_kda_timeline,
    plot_cs_trend,
    plot_champion_heatmap,
    plot_playstyles,
)
from utils.regions import REGION_MAP

# Load environment variables
load_dotenv()
RIOT_API_KEY = os.getenv("RIOT_API_KEY")

async def main():
    print("📊 Welcome to LoL Insight Tracker (Async Edition)")

    # Riot ID and Region
    riot_id = input("Enter your Riot ID (e.g., Summoner#TAG): ").strip()
    region_input = input("Enter region (e.g., NA, EUW, LAN): ").strip().upper()

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

    try:
        account = get_account_by_riot_id(game_name, tag_line, routing)
    except Exception as e:
        print(f"❌ Error fetching Riot account: {e}")
        return

    puuid = account["puuid"]

    print("📥 Fetching match history...")
    try:
        match_ids = get_match_ids(puuid, routing, count=20)
    except Exception as e:
        print(f"❌ Error fetching match IDs: {e}")
        return

    try:
        matches = await fetch_all_matches(match_ids, routing)
    except Exception as e:
        print(f"❌ Error fetching match data: {e}")
        return

    # Save raw matches locally
    os.makedirs("data", exist_ok=True)
    output_file = f"data/{game_name}_{tag_line}_{region_input}_matches.json"
    with open(output_file, "w") as f:
        json.dump(matches, f, indent=2)

    print("✅ Match data fetched and saved.")
    print("🔎 Running analysis...")

    try:
        df = add_trend_features(matches, puuid)
        df = classify_playstyle(df)

        plot_kda(df)
        plot_win_rate(df)
        plot_kda_timeline(df)
        plot_cs_trend(df)
        plot_champion_heatmap(df)
        plot_playstyles(df)

        print("🎯 Recommended Champions:")
        print(recommend_champions(df))
    except Exception as e:
        print(f"❌ Error during analysis: {e}")

if __name__ == "__main__":
    asyncio.run(main())
