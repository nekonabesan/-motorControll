from fastapi import APIRouter
from typing import List

import api.schemas.sensors.gyro.list as list_gyro_sensors_svhemas_api
import api.schemas.sensors.gyro.get.fas as fas_get_gyro_sensors_schemas
import api.schemas.sensors.gyro.get.angle as angle_get_gyro_sensors_schemas_api
import api.schemas.sensors.gyro.get.rate as rate_get_gyro_sensors_schemas
import api.schemas.sensors.gyro.set.calibration as calibration_set_yro_sensors_schemas

router = APIRouter()

# センサのディレクトリパスを取得
@router.get("/sensors/list", response_model=List[list_gyro_sensors_svhemas_api.List], status_code=201)
async def list_sensors():
    return [list_gyro_sensors_svhemas_api.List(gyro="/sys/class/lego-sensor/sensor0"
                            ,title="ジャイロセンサのディレクトリパスを返すメソッド")]

# センサーの生データ
@router.get("/sensors/gyro/get/fas", response_model=List[fas_get_gyro_sensors_schemas.Fas], status_code=201)
async def fas_get_gyro_sensors():
    return [fas_get_gyro_sensors_schemas.Fas(fas_a=0, fas_b=0, title="センサーの生データを返すメソッド")]

# 角度
@router.get("/sensors/gyro/get/angle", response_model=List[angle_get_gyro_sensors_schemas_api.Angle], status_code=201)
async def angle_get_gyro_sensors():
    return [angle_get_gyro_sensors_schemas_api.Angle(angle_a=0, angle_b=0, title="センサの指示角度を返すメソッド")]

# 回転速度(deg/sec)
@router.get("/sensors/gyro/get/rate", response_model=List[rate_get_gyro_sensors_schemas.Rate], status_code=201)
async def degrees_get_gyro_sensors():
    return[rate_get_gyro_sensors_schemas.Rate(rate_a=0, rate_b=0, title="センサの指示角速度[deg/s]を返すメソッド")]

# センサを校正
@router.get("/sensors/gyro/set/calibration")
async def calibration_set_gyro_sensors():
    pass