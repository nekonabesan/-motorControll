from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.sensors.list as list_sensors_schemas_api
import api.schemas.sensors.type as type_sensors_schemas_api
import api.schemas.sensors.gyro.set.modes as modes_set_gyro_sensors_schimas
import api.schemas.sensors.gyro.list as list_gyro_sensors_svhemas_api
import api.schemas.sensors.gyro.get.fas as fas_get_gyro_sensors_schemas
import api.schemas.sensors.gyro.get.angle as angle_get_gyro_sensors_schemas_api
import api.schemas.sensors.gyro.get.rate as rate_get_gyro_sensors_schemas
import api.schemas.sensors.gyro.set.calibration as calibration_set_yro_sensors_schemas
import api.service.connection.sensors.list as list_sensors_connection
import api.service.connection.sensors.type as type_sensors_connection
import api.service.connection.sensors.gyro.set.modes as modes_set_gyro_gyro_sensors_connection
import api.service.connection.connect_ev3_dev as connect_ev3_dev

router = APIRouter()

connection = connect_ev3_dev.connectEv3Dev()


# センサのディレクトリパスを取得
@router.get("/sensors/list", response_model=List[list_sensors_schemas_api.List], status_code=201)
async def list_sensors():
    getSensorsList = list_sensors_connection.getSensorsList()
    list = getSensorsList.command(connection)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [list_sensors_schemas_api.List(sensor_a=list[0], sensor_b=list[1])]

# センサのタイプを取得
@router.get("/sensors/type/{sensor_id}", response_model=List[type_sensors_schemas_api.Type], status_code=201)
async def list_sensors(sensor_id: str):
    getSensorsType = type_sensors_connection.getSensorsType()
    type = getSensorsType.command(connection, sensor_id)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [type_sensors_schemas_api.Type(type=type.replace('\n', ''))]

# ジャイロセンサーの初期設定
@router.get("/sensors/gyro/set/mode/{sensor_id}", response_model=List[modes_set_gyro_sensors_schimas.SetModes], status_code=201)
async def gyro_set_mode(sensor_id: str):
    setModes = modes_set_gyro_gyro_sensors_connection.SetModes()
    status = setModes.command(connection, sensor_id)
    return [modes_set_gyro_sensors_schimas.SetModes(status=status)]

# 角度(deg)と回転速度(deg/sec)
@router.get("/sensors/gyro/get/rate", response_model=List[rate_get_gyro_sensors_schemas.Rate], status_code=201)
async def degrees_get_gyro_sensors():
    return[rate_get_gyro_sensors_schemas.Rate(rate_a=0, rate_b=0, title="センサの指示角速度[deg/s]を返すメソッド")]

# センサを校正
@router.get("/sensors/gyro/set/calibration")
async def calibration_set_gyro_sensors():
    pass