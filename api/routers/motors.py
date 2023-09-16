from fastapi import APIRouter, HTTPException
from typing import List

import api.schemas.motors.init as init_motors_schima
import api.schemas.motors.list as list_motors_schemas
import api.schemas.motors.speed.set as set_speed_motors_schemas
import api.schemas.motors.speed.get as get_speed_motors_schemas
import api.schemas.motors.angle.get as get_angle_motors_schima
import api.schemas.motors.polarity.get as get_polarity_motors_schima
import api.schemas.motors.polarity.set as set_polarity_motors_schima
import api.service.connection.motor.init as init_mortor
import api.service.connection.motor.list as list_motors
import api.service.connection.motor.speed.get as get_speed
import api.service.connection.motor.speed.set as set_speed
import api.service.connection.motor.angle.get as get_angle
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

# モータに速度を指示するメソッド
@router.get("/motors/speed/set/{motor_id}/{speed}", response_model=List[set_speed_motors_schemas.Set], status_code=201)
async def set_speed_mortors(motor_id: str, speed: int):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    set = set_speed.Set()
    speed = set.command(connection, motor_id, speed)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [set_speed_motors_schemas.Set(speed=speed)]

@router.post("/motors/speed/set/{motor_id}/{speed}", response_model=List[set_speed_motors_schemas.Set], status_code=201)
async def set_speed_mortors(motor_id: str, speed: int):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    set = set_speed.Set()
    speed = set.command(connection, motor_id, speed)
    if list is None:
        connection = connect_ev3_dev.connectEv3Dev()
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [set_speed_motors_schemas.Set(speed=speed)]


# モータの速度を返すメソッド
@router.get("/motors/speed/get/{motor_id}", response_model=List[get_speed_motors_schemas.Get], status_code=201)
async def get_speed_mortors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    get = get_speed.Get()
    speed = get.command(connection, motor_id)
    if speed is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [get_speed_motors_schemas.Get(speed=speed)]

@router.post("/motors/speed/get/{motor_id}", response_model=List[get_speed_motors_schemas.Get], status_code=201)
async def get_speed_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    get = get_speed.Get()
    speed = get.command(connection, motor_id)
    if speed is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [get_speed_motors_schemas.Get(speed=speed)]

# モータの角度を返すメソッド
@router.get("/motors/angle/get/{motor_id}", response_model=List[get_angle_motors_schima.Get], status_code=201)
async def get_angle_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getAngle = get_angle.Get()
    angle = getAngle.command(connection, motor_id)
    if angle is None:
        connection = connect_ev3_dev.connectEv3Dev()
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return[get_angle_motors_schima.Get(angle=int(angle))]

# モータの極性を返すメソッド
@router.get("/motors/polarity/get/{motor_id}", response_model=List[get_polarity_motors_schima.Get], status_code=201)
async def get_polarity_motors(motor_id: str):
    global connection
    if connection is None:
        connection = connect_ev3_dev.connectEv3Dev()
    getPolarity = get_polarity.Get()
    property = getPolarity.command(connection, motor_id)
    if property is None:
        connection = connect_ev3_dev.connectEv3Dev()
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
        connection = connect_ev3_dev.connectEv3Dev()
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