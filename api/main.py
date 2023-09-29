from fastapi import FastAPI
from api.routers import motors, sensors

app = FastAPI()
app.include_router(motors.router)
app.include_router(sensors.router)