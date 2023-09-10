from pydantic import BaseModel, Field

class Angle(BaseModel):
    angle_a: int = Field(None, example=0)
    angle_b: int = Field(None, example=0)
    done: bool = Field(False, description="完了フラグ")