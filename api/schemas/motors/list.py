from typing import Optional
from pydantic import BaseModel, Field

class ListBase(BaseModel):
    motor_a: str = Field(None, example="motor0")
    motor_b: str = Field(None, example="motor1")

class List(ListBase):
    done: bool = Field(True, description="完了フラグ")
