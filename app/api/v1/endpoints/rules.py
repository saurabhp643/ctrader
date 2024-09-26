from fastapi import APIRouter
from app.core.event_producer import produce_event

router = APIRouter()

@router.post("/evaluate")
async def evaluate_rule(rule_data: dict):
    # Trigger a rule evaluation event
    produce_event('rule_evaluated', rule_data)
    return {"message": "Rule evaluated!"}
