from typing import Optional

from pydantic import BaseModel, Field


class List(BaseModel):
    gyro: str = Field(None, example="/sys/class/lego-sensor/sensor0")
    done: bool = Field(False, description="完了フラグ")