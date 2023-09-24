from pydantic import BaseModel, Field

class AngleBase(BaseModel):
    angle: int = Field(None, example=0)

class Angle(AngleBase):
    done: bool = Field(True, description="完了フラグ")