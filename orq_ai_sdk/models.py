from typing import Union

from pydantic import BaseModel


class UserInfo(BaseModel):
    id: Union[str, int, None] = None


Store = {}
