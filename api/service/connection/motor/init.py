import api.service.connection.connect_ev3_dev as connect

class Init():
     CMD = 'echo reset > /sys/class/tacho-motor/'
     def command(self, connection: connect.connectEv3Dev, motor_id: str):
          result = connection.sendForSet(self.CMD + motor_id  + '/command && echo 0')
          return result