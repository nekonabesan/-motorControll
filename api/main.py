from fastapi import FastAPI

from api.routers import motors, sensors

import api.models.connect_ev3_dev as connect_ev3_dev

ssh = connect_ev3_dev.connectEv3Dev()

def sshConnection():
    return ssh.client


app = FastAPI()
app.include_router(motors.router)
app.include_router(sensors.router)