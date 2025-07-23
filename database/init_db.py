# init_db.py

from datetime import datetime
from database.session import SessionLocal
from database.models import Match
import os
from dotenv import load_dotenv

load_dotenv()

# Crear sesión
session = SessionLocal()

# Crear objeto Match de ejemplo
new_match = Match(
    id="match_123",
    puuid="puuid_abc123",
    champion="Ahri",
    kills=10,
    deaths=2,
    assists=8,
    kda=5.0,
    cs=200,
    cs_per_min=8.5,
    win=True,
    timestamp=datetime.utcnow()
)

# Insertar en la base de datos
try:
    session.add(new_match)
    session.commit()
    print("¡Inserción exitosa!")
except Exception as e:
    session.rollback()
    print("Error al insertar:", e)
finally:
    session.close()
