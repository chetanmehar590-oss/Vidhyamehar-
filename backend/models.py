from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime
import uuid

class TableRequestOptions(BaseModel):
    freshId: bool = False
    codeAapDoge: bool = False
    noIPhone: bool = False
    noKingPass: bool = False
    autoLoss: bool = False

class TableRequest(BaseModel):
    username: str
    amount: str
    type: str
    gamePlus: str
    options: TableRequestOptions

class TableRequestDB(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str
    amount: str
    type: str
    gamePlus: str
    options: Dict[str, bool]
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    sent_to_telegram: bool = False