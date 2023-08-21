from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class WalletHistory(BaseModel):
    timestamp: str  # ISO timestamp
    value: float

class WalletBalance(BaseModel):
    wallet: str
    balance: float
    balance_usd: float
    history: List[WalletHistory]
    last_updated: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)
        self.last_updated = datetime.utcnow().isoformat()
