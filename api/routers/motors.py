from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.motors.init as init_motors_schima
import api.schemas.motors.list as list_motors_schemas
import api.schemas.motors.pwm_value.set as set_pwm_value_motors_schemas
import api.schemas.motors.pwm_value.pare as pare_pwm_value_motors_schemas
import api.schemas.motors.pwm_value.get as get_pwm_value_motors_schemas
import api.schemas.motors.dps.get as get_dps_mortors
import api.schemas.motors.count_per_rot.get as get_cpr_motors_schimas
import api.schemas.motors.angle.get as get_angle_motors_schima
import api.schemas.motors.polarity.get as get_polarity_motors_schima
import api.schemas.motors.polarity.set as set_polarity_motors_schima
import api.service.connection.motor.init as init_mortor
import api.service.connection.motor.list as list_motors
import api.service.connection.motor.pwm_value.get as get_pwm_value
import api.service.connection.motor.pwm_value.set as set_pwm_value
import api.service.connection.motor.pwm_value.pare as pare_pwm_value
import api.service.connection.motor.dps.get as get_dps_motor_connection
import api.service.connection.motor.angle.get as get_angle
import api.service.connection.motor.count_per_rot.get as get_cpr_motors_connection
import api.service.connection.motor.polarity.get as get_polarity
import api.service.connection.motor.polarity.set as set_polarity
import api.service.connection.connect_ev3_dev as connect_ev3_dev

router = APIRouter()

connection = connect_ev3_dev.connectEv3Dev()


# モータのディレクトリパスを返す
@router.get("/motors/list", response_model=List[list_motors_schemas.List], status_code=201)
async def list_mortors():
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getMortorslist = list_motors.getMotersList() 
    list = getMortorslist.command(connection)
    if list is None:
        raise HTTPException(status_code=400, detail="Dose Not Connect ev3")
    return [list_motors_schemas.List(motor_a=list[0], motor_b=list[1])]

@router.post("/motors/list", response_model=List[list_motors_schemas.List], status_code=201)
async def list_mortors():
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getMortorslist = list_motors.getMotersList()
    list = getMortorslist.command(connection)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [list_motors_schemas.List(motor_a=list[0], motor_b=list[1])]

# モータにデューティ比を指示するメソッド
@router.get("/motors/pwm_value/set/{motor_id}/{pwm_value}", response_model=List[set_pwm_value_motors_schemas.Set], status_code=201)
async def set_pwm_value_mortors(motor_id: str, pwm_value: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    set = set_pwm_value.Set()
    pwm_value = set.command(connection, motor_id, pwm_value)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [set_pwm_value_motors_schemas.Set(pwm_value=pwm_value)]

@router.post("/motors/pwm_value/set/{motor_id}/{pwm_value}", response_model=List[set_pwm_value_motors_schemas.Set], status_code=201)
async def set_pwm_value_mortors(motor_id: str, pwm_value: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    set = set_pwm_value.Set()
    pwm_value = set.command(connection, motor_id, pwm_value)
    if pwm_value is None:
        raise HTTPException(status_code=500, detail="Dose Not Set pwm_value")
    return [set_pwm_value_motors_schemas.Set(motor_id=motor_id, pwm_value=pwm_value)]

#モータ２基に同時にデューティ比を設定するメソッド
@router.get("/motors/pwm_value/set/pare/{motor_l_id}/{motor_r_id}/{pwm_value}", response_model=List[pare_pwm_value_motors_schemas.Pare], status_code=201)
async def set_pwm_value_mortors(motor_l_id: str, motor_r_id: str, pwm_value: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    pare = pare_pwm_value.Pare()
    pwm_value = pare.command(connection, motor_l_id, motor_r_id, pwm_value)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [pare_pwm_value_motors_schemas.Pare(motor_l_id=motor_l_id, motor_r_id=motor_r_id, pwm_value=pwm_value)]

# モータの設定を返すメソッド
@router.get("/motors/pwm_value/get/{motor_id}", response_model=List[get_pwm_value_motors_schemas.Get], status_code=201)
async def get_pwm_value_mortors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    get = get_pwm_value.Get()
    pwm_value = get.command(connection, motor_id)
    if pwm_value is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [get_pwm_value_motors_schemas.Get(pwm_value=pwm_value)]

@router.post("/motors/pwm_value/get/{motor_id}", response_model=List[get_pwm_value_motors_schemas.Get], status_code=201)
async def get_pwm_value_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    get = get_pwm_value.Get()
    pwm_value = get.command(connection, motor_id)
    if pwm_value is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [get_pwm_value_motors_schemas.Get(pwm_value=pwm_value)]

# モータの角度を返すメソッド
@router.get("/motors/angle/get/{motor_id}/", response_model=List[get_angle_motors_schima.Get], status_code=201)
async def get_angle_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getAngle = get_angle.Get()
    angle = getAngle.command(connection, motor_id)
    if angle is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[get_angle_motors_schima.Get(angle=int(angle))]

# モータのcount_per_rotを返すメソッド
@router.get("/motors/count_per_rot/get/{motor_id}", response_model=List[get_cpr_motors_schimas.Get], status_code=201)
async def get_angle_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getCpr = get_cpr_motors_connection.Get()
    cpr = getCpr.command(connection, motor_id)
    if cpr is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[get_cpr_motors_schimas.Get(cpr=int(cpr))]

# モータの角速度を返すメソッド
@router.get("/motors/dps/get/{motor_a_id}/{motor_b_id}", response_model=List[get_dps_mortors.Get], status_code=201)
async def get_angle_motors(motor_a_id: str, motor_b_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getDps = get_dps_motor_connection.Get()
    (motor_a_dps, motor_b_dps) = getDps.command(connection, motor_a_id, motor_b_id)
    if motor_a_dps is None or  motor_b_dps is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[get_dps_mortors.Get(motor_a_dps=int(motor_a_dps), motor_b_dps=int(motor_b_dps))]

# モータの極性を返すメソッド
@router.get("/motors/polarity/get/{motor_id}", response_model=List[get_polarity_motors_schima.Get], status_code=201)
async def get_polarity_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getPolarity = get_polarity.Get()
    property = getPolarity.command(connection, motor_id)
    if property is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[get_polarity_motors_schima.Get(polarity=property.replace('\n', ''))]

# モータの極性を設定するメソッド
@router.get("/motors/polarity/set/{motor_id}/{property}", response_model=List[set_polarity_motors_schima.Set], status_code=201)
async def get_polarity_motors(motor_id: str, property: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    setPolarity = set_polarity.Set()
    property = setPolarity.command(connection, motor_id, property)
    if property is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[set_polarity_motors_schima.Set(motor_id=motor_id, polarity=property.replace('\n', ''))]

# モータを初期化するメソッド
@router.get("/motors/init/{motor_id}", response_model=List[init_motors_schima.Init], status_code=201)
async def init_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    initMotor = init_mortor.Init()
    initMotor.command(connection, motor_id)
    return[init_motors_schima.Init(result=0)]