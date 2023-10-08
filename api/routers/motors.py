from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.motors.pwm_value.set as set_pwm_value_motors_schemas
import api.schemas.motors.pwm_value.pare as pare_pwm_value_motors_schemas
import api.schemas.motors.dps.get as get_dps_mortors
import api.schemas.motors.position.get as get_cpr_motors_schimas
import api.schemas.motors.aposition.get as get_angle_motors_schima
import api.schemas.motors.run_for_degrees.set as set_degrees_for_run_motors_schima
import api.schemas.motors.run_for_degrees.pair as pair_degrees_for_run_motors_schima
import api.service.connection.motors.pwm_value.get as get_pwm_value
import api.service.connection.motors.pwm_value.set as set_pwm_value
import api.service.connection.motors.pwm_value.pare as pare_pwm_value
import api.service.connection.motors.dps.get as get_dps_motor_connection
import api.service.connection.motors.aposition.get as get_angle
import api.service.connection.connect_motors as connect_motors
import api.service.connection.motors.run_for_degrees.set as set_degrees_for_run_motor_connection
import api.service.connection.motors.run_for_degrees.pair as pair_degrees_for_run_motor_connection

router = APIRouter()

connection = connect_motors.connectMotors()

# モータにデューティ比を指示するメソッド
@router.get("/motors/pwm_value/set/{motor_id}/{pwm_value}", response_model=List[set_pwm_value_motors_schemas.Set], status_code=201)
async def set_pwm_value_mortors(motor_id: str, pwm_value: int):
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    set = set_pwm_value.Set()
    pwm_value = set.command(connection, motor_id, pwm_value)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [set_pwm_value_motors_schemas.Set(pwm_value=pwm_value)]

@router.post("/motors/pwm_value/set/{motor_id}/{pwm_value}", response_model=List[set_pwm_value_motors_schemas.Set], status_code=201)
async def set_pwm_value_mortors(motor_id: str, pwm_value: str):
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    set = set_pwm_value.Set()
    pwm_value = set.command(connection, motor_id, pwm_value)
    if pwm_value is None:
        raise HTTPException(status_code=500, detail="Dose Not Set pwm_value")
    return [set_pwm_value_motors_schemas.Set(motor_id=motor_id, pwm_value=pwm_value)]

#モータ２基に同時にデューティ比を設定するメソッド
@router.get("/motors/pwm_value/set/pare/{pwm_value}", response_model=List[pare_pwm_value_motors_schemas.Pare], status_code=201)
async def set_pwm_value_mortors(pwm_value: str):
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    pare = pare_pwm_value.Pare()
    pwm_value = pare.command(connection, pwm_value)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [pare_pwm_value_motors_schemas.Pare(pwm_value=pwm_value)]

# モーターの絶対位置を返すメソッド
@router.get("/motors/get_aposition/get/", response_model=List[get_angle_motors_schima.Get], status_code=201)
async def get_angle_motors():
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    getAposition = get_angle.Get()
    (motor_a_aposition,motor_b_aposition) = getAposition.command(connection)
    if motor_a_aposition is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect")
    return[get_angle_motors_schima.Get(motor_a_aposition=motor_a_aposition, motor_b_aposition=motor_b_aposition)]

# リセット位置を基準としたモーターの位置を返すメソッド
@router.get("/motors/get_position/get/{motor_id}", response_model=List[get_cpr_motors_schimas.Get], status_code=201)
async def get_angle_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    getCpr = get_pwm_value.Get()
    cpr = getCpr.command(connection, motor_id)
    if cpr is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[get_cpr_motors_schimas.Get(cpr=int(cpr))]

# モータの角速度を返すメソッド
@router.get("/motors/dps/get/", response_model=List[get_dps_mortors.Get], status_code=201)
async def get_angle_motors():
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    getDps = get_dps_motor_connection.Get()
    (motor_a_dps, motor_b_dps) = getDps.command(connection)
    if motor_a_dps is None or  motor_b_dps is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect")
    return[get_dps_mortors.Get(motor_a_dps=int(motor_a_dps), motor_b_dps=int(motor_b_dps))]

# モータへ回転角度を指示
@router.get("/motors/run_for_degrees/set/{motor_id}/{degree}/{pwm_value}/{blocking}/", response_model=List[set_degrees_for_run_motors_schima.Set], status_code=201)
async def get_angle_motors(motor_id: str, degree: int, pwm_value: int, blocking: int):
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    setRunForDegrees = set_degrees_for_run_motor_connection.Set()
    degree = int(setRunForDegrees.command(connection, motor_id, degree, pwm_value, blocking))
    if degree is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect")
    return[set_degrees_for_run_motors_schima.Set(motor_id=motor_id, degree=degree, pwm_value=pwm_value, blocking=blocking)]

# モータ2基へ回転角度を指示
@router.get("/motors/run_for_degrees/set/pare/{degree}/{pwm_value}/{blocking}", response_model=List[pair_degrees_for_run_motors_schima.Pair], status_code=201)
async def set_run_for_degree(motor_id: str, degree: int, pwm_value: int, blocking: int):
    global connection
    if connection is None:
        connection = connect_motors.connectMotors()
    degree = setRunForDegrees = pair_degrees_for_run_motor_connection.Pair()
    degree = setRunForDegrees.command(connection, degree, pwm_value, blocking)
    if degree is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect")
    return[pair_degrees_for_run_motors_schima.Pair(motor_id=motor_id, degree=degree, pwm_value=pwm_value, blocking=blocking)]