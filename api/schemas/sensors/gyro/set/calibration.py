from pydantic import BaseModel, Field

class CalibrationBase(BaseModel):
    degrees_a: int = Field(None, example="")
    degrees_a: int = Field(None, example="")

class Calibration(CalibrationBase):
    done: bool = Field(True, description="完了フラグ")