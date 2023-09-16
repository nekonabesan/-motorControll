import api.service.connection.connect_ev3_dev as connect

class Set():
    # echo run-direct > /sys/class/tacho-motor/motor0/polarity
    PATH = '/sys/class/tacho-motor/'
    def command(self, connection: connect.connectEv3Dev, motor_id: str, polarity: str):
        connection.sendForSet('echo ' + polarity + '> ' + self.PATH  + motor_id + '/polarity && '
            'cat ' + self.PATH + motor_id + '/polarity')
        return polarity