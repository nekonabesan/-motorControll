from typing import Optional

from pydantic import BaseModel, Field

class SetBase(BaseModel):
    motor_id:  str = Field(None, example="/sys/class/tacho-motor/motor0")
    speed: int = Field(None, example=10)

class Set(SetBase):
    done: bool = Field(True, description="完了フラグ")