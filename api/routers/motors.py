from fastapi import APIRouter, HTTPException
from typing import List


import api.schemas.motors.list as list_motors_schemas
import api.schemas.motors.speed.set as set_speed_motors_schemas
import api.schemas.motors.speed.get as get_speed_motors_schemas
import api.models.motor.list as motors_list
import api.models.motor.speed.get as get_speed
import api.models.motor.speed.set as set_speed
import api.models.connect_ev3_dev as connect_ev3_dev

router = APIRouter()

connection = connect_ev3_dev.connectEv3Dev()


# モータのディレクトリパスを返す
@router.get("/motors/list", response_model=List[list_motors_schemas.List], status_code=201)
async def list_mortors():
    getMortorslist = motors_list.getMotersList()
    list = getMortorslist.command(connection)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [list_motors_schemas.List(motor_a=list[0], motor_b=list[1])]

@router.post("/motors/list", response_model=List[list_motors_schemas.List], status_code=201)
async def list_mortors():
    getMortorslist = motors_list.getMotersList()
    list = getMortorslist.command(connection)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [list_motors_schemas.List(motor_a=list[0], motor_b=list[1])]

# モータに速度を指示するメソッド
@router.get("/motors/speed/set/{motor_id}/{speed}", response_model=List[set_speed_motors_schemas.Set], status_code=201)
async def set_speed_mortors(motor_id: str, speed: int):
    set = set_speed.Set()
    speed = set.command(connection, motor_id, speed)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [set_speed_motors_schemas.Set(speed=speed)]

@router.post("/motors/speed/set/{motor_id}/{speed}", response_model=List[set_speed_motors_schemas.Set], status_code=201)
async def set_speed_mortors(motor_id: str, speed: int):
    set = set_speed.Set()
    speed = set.command(connection, motor_id, speed)
    if list is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [set_speed_motors_schemas.Set(speed=speed)]


# モータの速度を返すメソッド
@router.get("/motors/speed/get/{motor_id}", response_model=List[get_speed_motors_schemas.Get], status_code=201)
async def get_speed_mortors(motor_id: str):
    get = get_speed.Get()
    speed = get.command(connection, motor_id)
    if speed is None:
        raise HTTPException(status_code=500, detail="Dose Not Connect ev3")
    return [get_speed_motors_schemas.Get(speed=speed)]

@router.post("/motors/speed/get/{motor_id}", response_model=List[get_speed_motors_schemas.Get], status_code=201)
async def get_speed_mortors(motor_id: str):
    return [get_speed_motors_schemas.Get(motor_id=motor_id)]
