from pydantic import BaseModel, Field

class GetBase(BaseModel):
    gyro_angle: int = Field(None, example=0)
    gyro_dps: int = Field(None, example=0)
    motor_a_dps: int = Field(None, example=0)
    motor_b_dps: int = Field(None, example=0)
    motor_a_position: int = Field(None, example=0)
    motor_b_position: int = Field(None, example=0)

class Get(GetBase):
    done: bool = Field(True, description="完了フラグ")