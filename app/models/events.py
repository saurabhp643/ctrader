from pydantic import BaseModel

class Event(BaseModel):
    event_id: int
    event_name: str
    event_data: dict
    occurred_at: str
