# 🧠 LoL Insight — League of Legends Personal Stats Tracker

**LoL Insight** is a modular Python application that fetches and analyzes match history data from the **Riot Games API**. It provides personalized visualizations, gameplay trend analysis, and champion performance insights to help you track your progression and identify areas for improvement — just like OP.GG or League of Graphs, but tailored to your own profile.

---

## 📦 Features

- 🔎 Search summoners by Riot ID (e.g. `Faker#KR1`) across all supported regions
- 🎮 Fetch and store match history (Match-V5)
- 📈 Visualize key metrics like:
  - KDA over time
  - CS per minute trends
  - Win rate per champion
- 🧪 Profile playstyle: Aggressive, Passive, Supportive, Balanced
- 🌡 Champion heatmaps (KDA, CS/min, Win Rate)
- 🧠 Recommend champions based on personal performance data

---

## 🚀 Getting Started

### 1. Clone the repository

-bash-

git clone https://github.com/yourusername/lol-insight.git
cd lol-insight

2. Create and activate a virtual environment

   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

4. Install dependencies

   pip install -r requirements.txt

4. Add your Riot API key

   Create a file named .env in the root directory and add:

   RIOT_API_KEY=your_riot_api_key_here

   ⚠️ Note: API keys from Riot expire every 24 hours in development mode. Refresh as needed from Riot Developer Portal.

🧠 Usage
-bash-

python main.py

Then follow the prompts:

Enter your Riot ID (SummonerName#Tag)

Enter your region (NA, EUW, LAN, etc.)

Visualizations and summaries will be generated automatically based on your recent matches.

🧰 Tech Stack
Python 3.10+

Riot API (Account-V1, Match-V5)

pandas, matplotlib, seaborn

dotenv for secure config

Modular folder-based architecture

📈 Roadmap
 Streamlit dashboard UI

 Champion matchup analytics

 Machine learning clustering for playstyle

 Discord bot for post-match reports

 Export to CSV/PDF/HTML

📄 License
MIT License

Made with ❤️ for educational and personal growth purposes.
Not affiliated with Riot Games.
