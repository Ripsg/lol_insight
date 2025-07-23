# 1. Importa la sesión de SQLAlchemy y el modelo
from database.session import SessionLocal
from database.models import Match
from datetime import datetime

# 2. Crea una nueva sesión
session = SessionLocal()

# 3. Crea un objeto Match
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

# 4. Lo guarda en la base de datos
try:
    session.add(new_match)
    session.commit()
    print("¡Inserción exitosa!")
except Exception as e:
    session.rollback()
    print("Error al insertar:", e)
finally:
    session.close()
