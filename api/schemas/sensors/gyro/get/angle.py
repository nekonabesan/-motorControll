from pydantic import BaseModel, Field

class Angle(BaseModel):
    angle: int = Field(None, example=0)
    done: bool = Field(False, description="完了フラグ")