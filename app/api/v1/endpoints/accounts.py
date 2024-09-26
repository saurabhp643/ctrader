from fastapi import APIRouter
from app.core.event_producer import produce_event

router = APIRouter()

@router.post("/create")
async def create_account(account_data: dict):
    # Trigger the event producer
    produce_event('account_created', account_data)
    return {"message": "Account created!"}
