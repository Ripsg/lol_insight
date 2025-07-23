import requests
import aiohttp
import asyncio
from config import RIOT_API_KEY

def get_match_ids(puuid, routing, count=20):
    url = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    return requests.get(url, headers=headers).json()

async def _fetch(session, match_id, routing):
    url = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    async with session.get(url, headers=headers) as r:
        return await r.json() if r.status == 200 else None

async def fetch_all_matches(match_ids, routing):
    async with aiohttp.ClientSession() as s:
        tasks = [_fetch(s, mid, routing) for mid in match_ids]
        return [m for m in await asyncio.gather(*tasks) if m]
