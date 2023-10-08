import api.service.connection.connect_motors as connect

class Pare():
    def command(self, connection: connect.connectMotors, pwm_value: int):
        connection.pare.set_default_speed(pwm_value)
        connection.pare.start()
        return pwm_value