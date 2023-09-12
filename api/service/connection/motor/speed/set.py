import api.service.connection.connect_ev3_dev as connect

class Set():
    # echo run-direct > /sys/class/tacho-motor/motor0/command && echo 0 > /sys/class/tacho-motor/motor0/duty_cycle_sp && cat /sys/class/tacho-motor/motor0/duty_cycle_sp
    PATH = '/sys/class/tacho-motor/'
    def command(self, connection: connect.connectEv3Dev, motor_id: str, speed: int):
        connection.sendForSet('echo run-direct > ' + self.PATH  + motor_id + '/command && '
            'echo ' + str(speed) + ' > ' + self.PATH + motor_id + '/duty_cycle_sp && '
            'cat ' + self.PATH + motor_id + '/duty_cycle_sp')
        return speed