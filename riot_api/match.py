import requests
import aiohttp
import asyncio
from config import RIOT_API_KEY

# ------------------------------
# 1. Obtener lista de match IDs
# ------------------------------

def get_match_ids(puuid, routing, count=20):
    """
    Usa el puuid del jugador para obtener los IDs de sus partidas recientes.

    Parámetros:
    - puuid: Identificador único del jugador
    - routing: Región de enrutamiento para Match-V5 (e.g. americas, europe)
    - count: Número de partidas a recuperar

    Retorna:
    - Lista de strings con los IDs de las partidas
    """
    url = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={count}"
    headers = {"X-Riot-Token": RIOT_API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


# ----------------------------------
# 2. Obtener detalles de cada match
# ----------------------------------

async def fetch_match(session, match_id, routing):
    """
    Función asíncrona para obtener los detalles de una sola partida.

    Parámetros:
    - session: Sesión aiohttp activa
    - match_id: ID de la partida
    - routing: Región de enrutamiento para Match-V5

    Retorna:
    - JSON con los detalles de la partida
    """
    url = f"https://{routing}.api.riotgames.com/lol/match/v5/matches/{match_id}"
    headers = {"X-Riot-Token": RIOT_API_KEY}

    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"⚠️ Error {response.status} al obtener partida {match_id}")
            return None


async def fetch_all_matches(match_ids, routing):
    """
    Llama en paralelo a fetch_match para todas las partidas.

    Parámetros:
    - match_ids: Lista de IDs de partidas
    - routing: Región de enrutamiento

    Retorna:
    - Lista de objetos JSON con los datos de cada partida
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_match(session, match_id, routing) for match_id in match_ids]
        results = await asyncio.gather(*tasks)
        # Filtramos partidas inválidas (None)
        return [match for match in results if match is not None]
