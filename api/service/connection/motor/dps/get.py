import api.service.connection.connect_ev3_dev as connect

class Get():
    CMD = 'cat /sys/class/tacho-motor/'
    def command(self, connection: connect.connectEv3Dev, motor_a_id: str, motor_b_id: str):
        motor_a_dps = int(connection.sendForGet(self.CMD + motor_a_id + '/speed'))
        motor_b_dps = int(connection.sendForGet(self.CMD + motor_b_id + '/speed'))
        return motor_a_dps, motor_b_dps