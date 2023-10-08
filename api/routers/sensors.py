from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()


# ジャイロセンサーのモード設定
@router.get("/sensors/gyro/set/mode/")
async def gyro_set_mode():
    pass
