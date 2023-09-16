from typing import Optional

from pydantic import BaseModel, Field

class SetBase(BaseModel):
    motor_id:  str = Field(None, example="motor0")
    polarity: str = Field(None, example='normal')

class Set(SetBase):
    done: bool = Field(True, description="完了フラグ")