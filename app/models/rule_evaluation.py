from pydantic import BaseModel

class RuleEvaluation(BaseModel):
    rule_id: int
    rule_name: str
    result: bool
    executed_at: str
