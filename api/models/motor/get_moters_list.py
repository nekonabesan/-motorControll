import api.models.connect_ev3_dev as connect

class getMotersList():
     CMD = 'for f in /sys/class/tacho-motor/*; do echo $f; done'
     def command(self):
          motors = []
          connector = connect.connectEv3Dev()
          motors = connector.send(self.CMD)
          return motors
     

