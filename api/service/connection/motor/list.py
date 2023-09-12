import api.service.connection.connect_ev3_dev as connect

class getMotersList():
     CMD = 'for f in /sys/class/tacho-motor/*; do echo $f; done'
     def command(self, connection: connect.connectEv3Dev):
          motors = []
          motors = connection.sendForSensorsList(self.CMD)
          return motors
     

