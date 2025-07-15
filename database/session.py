import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

load_dotenv()

POSTGRES_URL = os.getenv("POSTGRES_URL")  # e.g. postgresql://user:pwd@localhost/lol_insight

engine = create_engine(POSTGRES_URL, pool_pre_ping=True, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))
