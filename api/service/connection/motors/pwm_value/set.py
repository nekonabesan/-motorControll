import api.service.connection.connect_motors as connect

class Set():
    def command(self, connection: connect.connectMotors, motor_id: str, pwm_value: int):
        if motor_id == 'A':
            connection.motor_a.set_default_speed(pwm_value)
            connection.motor_a.start()
        elif motor_id == 'B':
            connection.motor_b.set_default_speed(pwm_value)
            connection.motor_b.start()
        return pwm_value