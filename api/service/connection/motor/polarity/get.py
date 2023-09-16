import api.service.connection.connect_ev3_dev as connect

class Get():
    CMD = 'cat /sys/class/tacho-motor/'
    def command(self, connection: connect.connectEv3Dev, motor_id: str):
        polarity = connection.sendForGet(self.CMD + motor_id + '/polarity')
        print(polarity)
        return polarity