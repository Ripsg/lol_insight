import asyncio
from datetime import datetime
from sqlalchemy import select
from database.session import SessionLocal
from database.models import Match
from riot_api.match import get_match_ids, fetch_all_matches
from analysis.trends import add_trend_features   # to parse stats quickly

# ---------- high-level API ---------- #

def load_matches(puuid: str, routing: str, count: int = 20):
    """Return list[Match] models (DB) for given player; fetch new ones if needed."""
    with SessionLocal() as db:
        # ids already stored
        stored_ids = {m.id for m in db.scalars(select(Match.id).where(Match.puuid == puuid))}
        wanted_ids = get_match_ids(puuid, routing, count)
        new_ids = [mid for mid in wanted_ids if mid not in stored_ids]

        if new_ids:
            new_raw = asyncio.run(fetch_all_matches(new_ids, routing))
            _persist_matches(db, new_raw, puuid)
        return db.scalars(select(Match).where(Match.puuid == puuid)).all()

# ---------- helpers ---------- #

def _persist_matches(db, raw_matches, puuid):
    df = add_trend_features(raw_matches, puuid)  # re-uses your parser
    for row, raw in zip(df.to_dict("records"), raw_matches):
        db.add(Match(
            id          = raw["metadata"]["matchId"],
            puuid       = puuid,
            champion    = row["champion"],
            kills       = row["kills"],
            deaths      = row["deaths"],
            assists     = row["assists"],
            kda         = row["KDA"],
            cs          = row["cs"],
            cs_per_min  = row["CS_per_min"],
            win         = row["win"],
            timestamp   = row["timestamp"]
        ))
    db.commit()
