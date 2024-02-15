from functools import lru_cache
from typing import Optional

from pydantic import BaseModel


class UserInfo(BaseModel):
    id: str | int


Store = {}
