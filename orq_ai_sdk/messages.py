from typing import Literal
from pydantic import BaseModel


class Message(BaseModel):
    _role: Literal["user", "assistant"]
    content: str

    @property
    def role(self):
        return self._role

    def to_dict(self):
        return {"role": self.role, "content": self.content}


class UserMessage(Message):
    _role: Literal["user"] = "user"


class AssistantMessage(Message):
    _role: Literal["assistant"] = "assistant"
