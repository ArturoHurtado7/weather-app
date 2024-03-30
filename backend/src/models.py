from datetime import datetime

from sqlalchemy import Column, String, DateTime, JSON

from src.database import Base

class Cache(Base):
    __tablename__ = "cache"
    id = Column(String(50), primary_key=True)
    data = Column(JSON)
    date = Column(
        DateTime, index=True, default=datetime.now, onupdate=datetime.now
    )
