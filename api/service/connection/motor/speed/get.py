import api.service.connection.connect_ev3_dev as connect

class Get():
    CMD = 'cat /sys/class/tacho-motor/'
    def command(self, connection: connect.connectEv3Dev, motor_id: str):
        speed = int(connection.sendForGet(self.CMD + motor_id + '/duty_cycle_sp'))
        return speed