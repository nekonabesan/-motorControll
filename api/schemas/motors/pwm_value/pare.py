from typing import Optional

from pydantic import BaseModel, Field

class PareBase(BaseModel):
    motor_l_id:  str = Field(None, example="motor0")
    motor_r_id:  str = Field(None, example="motor0")
    pwm_value: int = Field(None, example=10, ge=-100, le=100)

class Pare(PareBase):
    done: bool = Field(True, description="完了フラグ")