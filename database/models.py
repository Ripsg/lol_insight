from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Boolean, DateTime, func

class Base(DeclarativeBase):
    pass


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[str]       = mapped_column(String, primary_key=True)
    puuid: Mapped[str]    = mapped_column(String, index=True)
    champion: Mapped[str] = mapped_column(String)
    kills: Mapped[int]
    deaths: Mapped[int]
    assists: Mapped[int]
    kda: Mapped[float]
    cs: Mapped[int]
    cs_per_min: Mapped[float]
    win: Mapped[bool]
    timestamp: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
