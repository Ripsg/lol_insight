from database.session import SessionLocal
from database.models import Match

# Crear sesión
session = SessionLocal()

try:
    matches = session.query(Match).all()
    for m in matches:
        print(f"{m.id} | {m.champion} | {m.kills}/{m.deaths}/{m.assists} | Win: {m.win}")
except Exception as e:
    print("Error al leer:", e)
finally:
    session.close()
