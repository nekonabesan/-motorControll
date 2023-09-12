from typing import Optional

from pydantic import BaseModel, Field

class TypeBase(BaseModel):
    type: str = Field(None, example="lego-ev3-touch")

class Type(TypeBase):
    done: bool = Field(True, description="完了フラグ")