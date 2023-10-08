import api.service.connection.connect_motors as connect

class Get():
    def command(self, connection: connect.connectMotors):
        motor_a_dps = int(connection.motor_a.get_speed())
        motor_b_dps = int(connection.motor_b.get_speed())
        return motor_a_dps, motor_b_dps