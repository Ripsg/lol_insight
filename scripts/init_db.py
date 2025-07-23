# scripts/init_db.py
from database.session import engine
from database.models import Base

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("✅  Tabla 'matches' creada (o ya existía)")
