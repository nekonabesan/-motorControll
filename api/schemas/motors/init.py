from pydantic import BaseModel, Field

class InitBase(BaseModel):
    result: int = Field(None, example=0)

class Init(InitBase):
    done: bool = Field(True, description="完了フラグ")