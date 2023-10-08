import api.service.connection.connect_motors as connect

class Set():
    def command(self, connection: connect.connectMotors, motor_id: str, degree: int, pwm_value: int, blocking: int):
        if motor_id == 'A':
            connection.motor_a.run_for_degrees(degree, pwm_value, False)
        elif motor_id == 'B':
            connection.motor_b.run_for_degrees(degree, pwm_value, False)
        return degree