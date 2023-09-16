from pydantic import BaseModel, Field

class Speed(BaseModel):
    speed: int = Field(None, example=0)
    done: bool = Field(False, description="完了フラグ")