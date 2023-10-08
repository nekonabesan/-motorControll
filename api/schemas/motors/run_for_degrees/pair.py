from typing import Optional

from pydantic import BaseModel, Field

class PairBase(BaseModel):
    motor_id: str = Field(None) 
    degree: int = Field(None, ge=-180, le=180)
    pwm_value: int = Field(None, example=10, ge=-100, le=100)
    blocking: int = Field(None, example=1, ge=0, le=1)

class Pair(PairBase):
    done: bool = Field(True, description="完了フラグ")