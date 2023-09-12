from typing import Optional

from pydantic import BaseModel, Field

class SetModesBase(BaseModel):
    status: int = Field(None, example=0)

class SetModes(SetModesBase):
    done: bool = Field(True, description="完了フラグ")