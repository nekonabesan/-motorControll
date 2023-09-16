from pydantic import BaseModel, Field

class GetBase(BaseModel):
    polarity: str = Field(None, example='normal')

class Get(GetBase):
    done: bool = Field(True, description="完了フラグ")