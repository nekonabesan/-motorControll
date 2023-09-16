from pydantic import BaseModel, Field

class GetBase(BaseModel):
    angle: int = Field(None, example=0)

class Get(GetBase):
    done: bool = Field(True, description="完了フラグ")