from typing import Optional
from pydantic import BaseModel, Field

class ListBase(BaseModel):
    sensor_a: str = Field(None, example="sensor0")
    sensor_b: str = Field(None, example="sensor1")

class List(ListBase):
    done: bool = Field(True, description="完了フラグ")
