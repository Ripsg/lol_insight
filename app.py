import streamlit as st
from dotenv import load_dotenv
from utils.regions import REGION_MAP
from riot_api.account import get_account_by_riot_id
from data_access.match_service import load_matches
from analysis.trends import add_trend_features
from analysis.profiling import classify_playstyle
from analysis.recommendation import recommend_champions
from visualizations.plots import plot_kda, plot_win_rate
from visualizations.advanced import (
    plot_kda_timeline, plot_cs_trend,
    plot_champion_heatmap, plot_playstyles
)

load_dotenv()
st.set_page_config("LoL Insight", layout="wide")
st.title("📊 LoL Insight")

# --- sidebar inputs ---------------------------------------------------------
with st.sidebar:
    riot_id    = st.text_input("Riot ID", placeholder="Faker#KR1")
    region_key = st.selectbox("Region", list(REGION_MAP))
    count      = st.slider("Matches to analyze", 10, 100, 20)
    run_btn    = st.button("Run analysis")

if not run_btn:
    st.info("Enter Riot ID and click *Run analysis*")
    st.stop()

# --- validation -------------------------------------------------------------
if "#" not in riot_id:
    st.error("Format must be *Name#Tag*")
    st.stop()

game_name, tag_line = riot_id.split("#")
platform, routing   = REGION_MAP[region_key]

# --- data pipeline ----------------------------------------------------------
try:
    account = get_account_by_riot_id(game_name, tag_line, routing)
except Exception as e:
    st.error(f"Account lookup failed: {e}")
    st.stop()

puuid = account["puuid"]

with st.spinner("Loading matches (cached in PostgreSQL)…"):
    matches_db = load_matches(puuid, routing, count)

# Convert DB rows back to DataFrame for analysis
import pandas as pd
df = pd.DataFrame([m.__dict__ for m in matches_db])
df = classify_playstyle(df)          # already has trend fields from DB

# --- Dashboards -------------------------------------------------------------
st.subheader("Summary table")
st.dataframe(df[["timestamp","champion","kills","deaths","assists","KDA","CS_per_min","playstyle"]], height=300)

col1, col2 = st.columns(2)
with col1:
    plot_kda(df)
    plot_kda_timeline(df)
with col2:
    plot_win_rate(df)
    plot_cs_trend(df)

st.subheader("Heatmap & Playstyles")
plot_champion_heatmap(df)
plot_playstyles(df)

st.subheader("Top champion recommendations")
st.table(recommend_champions(df))
