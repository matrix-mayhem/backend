from app.db.mongo import logs_collection
from datetime import datetime

async def log_event(event_type: str, data: dict):
    log = {
        "event_type": event_type,
        "data": data,
        "timestamp": datetime.utcnow()
    }

    await logs_collection.insert_one(log)