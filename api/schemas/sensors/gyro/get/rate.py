from pydantic import BaseModel, Field

class Rate(BaseModel):
    rate_a: int = Field(None, example=0)
    rate_b: int = Field(None, example=0)
    done: bool = Field(False, description="完了フラグ")