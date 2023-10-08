import api.service.connection.connect_motors as connect

class Get():
    def command(self, connection: connect.connectMotors, motor_id: str):
        if motor_id == 'A':
            pwm_value = int(connection.motor_a.get_speed())
        elif motor_id == 'B':
            pwm_value = int(connection.motor_b.get_speed())
        return pwm_value