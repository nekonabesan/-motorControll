import api.service.connection.connect_motors as connect

class Get():
    def command(self, connection: connect.connectMotors):
        motor_a_aposition = int(connection.motor_a.get_aposition())
        motor_b_aposition = int(connection.motor_b.get_aposition())
        return motor_a_aposition,motor_b_aposition