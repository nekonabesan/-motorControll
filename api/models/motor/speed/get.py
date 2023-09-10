import api.models.connect_ev3_dev as connect

class Get():
    CMD = 'cat /sys/class/tacho-motor/'
    def command(self, motor_id: str):
        speed = None
        connector = connect.connectEv3Dev()
        speed = connector.send(self.CMD + motor_id + '/speed_sp')
        speed = speed[0]
        return speed