from pydantic import BaseModel, Field

class GetBase(BaseModel):
    motor_a_aposition: int = Field(None, example=0)
    motor_b_aposition: int = Field(None, example=0)

class Get(GetBase):
    done: bool = Field(True, description="完了フラグ")