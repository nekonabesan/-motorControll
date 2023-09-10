from pydantic import BaseModel, Field

class calibration(BaseModel):
    degrees_a: int = Field(None, example="")
    degrees_a: int = Field(None, example="")
    done: bool = Field(False, description="完了フラグ")