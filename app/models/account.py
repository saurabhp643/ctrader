from pydantic import BaseModel

class Account(BaseModel):
    account_id: int
    account_name: str
    email: str
    created_at: str
