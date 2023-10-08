import time
import logging
import subprocess
from buildhat import Motor
from buildhat import MotorPair

class connectMotors():
    MOTOR_NAME_A = 'A'
    MOTOR_NAME_B = 'B'

    motor_a = None
    motor_b = None
    pare = None
    logger = None
    
    def __init__(self):
        self.motor_a = Motor(self.MOTOR_NAME_A)
        self.motor_b = Motor(self.MOTOR_NAME_B)
        #self.pare = MotorPair(self.MOTOR_NAME_A, self.MOTOR_NAME_B)

    def __del__(self):
        return True