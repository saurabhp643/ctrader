from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
async def get_all_events():
    # Return mock list of events
    return [{"event_id": 1, "name": "User Registered"}, {"event_id": 2, "name": "Account Updated"}]
