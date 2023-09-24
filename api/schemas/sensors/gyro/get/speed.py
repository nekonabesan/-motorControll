from pydantic import BaseModel, Field

class SpeedBase(BaseModel):
    speed: int = Field(None, example=0)

class Speed(SpeedBase):
    done: bool = Field(True, description="完了フラグ")