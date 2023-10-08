import api.service.connection.connect_motors as connect

class Pair():
    def command(self, connection: connect.connectMotors, degree: int, pwm_value: int, blocking: int):
        connection.pare.run_for_degrees(degree, pwm_value, False)