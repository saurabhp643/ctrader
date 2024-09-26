from fastapi import FastAPI
from app.api.v1.endpoints import accounts, events, rules

app = FastAPI()

app.include_router(accounts.router, prefix="/accounts")
app.include_router(events.router, prefix="/events")
app.include_router(rules.router, prefix="/rules")
