from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TokenData(BaseModel):
    user_id: str
    exp: Optional[int] = None

    @property
    def get_expiry_time(self):

        return datetime.fromtimestamp(self.exp)