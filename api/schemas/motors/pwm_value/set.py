from typing import Optional

from pydantic import BaseModel, Field

class SetBase(BaseModel):
    motor_id:  str = Field(None, example="motor0")
    pwm_value: int = Field(None, example=10, ge=-100, le=100)

class Set(SetBase):
    done: bool = Field(True, description="完了フラグ")