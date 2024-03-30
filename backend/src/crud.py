import datetime

from sqlalchemy.orm import Session
from sqlalchemy.dialects.mysql import insert

from src import models
from src.constants import CACHE_HOLD_MINUTES


def get_cache(db: Session, cache_id: str):
    """
    Get cache item from database
    """
    two_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=CACHE_HOLD_MINUTES)
    cache_item = db.query(models.Cache).filter(
        models.Cache.id == cache_id, 
        models.Cache.date >= two_minutes_ago
    ).first()
    return cache_item


def upsert_cache(db: Session, cache_id: str, cache: dict):
    """
    Upsert cache item in database
    """
    stmt = insert(models.Cache).values(
        id=cache_id,
        data=cache,
        date=datetime.datetime.now()
    )
    stmt = stmt.on_duplicate_key_update(
        data=stmt.inserted.data,
        date=stmt.inserted.date
    )
    db.execute(stmt)
    db.commit()
