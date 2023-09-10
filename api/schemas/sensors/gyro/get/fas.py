from typing import Optional

from pydantic import BaseModel, Field


class Fas(BaseModel):
    fas_a: int = Field(None, example=0)
    fas_b: int = Field(None, example=0)
    done: bool = Field(False, description="完了フラグ")