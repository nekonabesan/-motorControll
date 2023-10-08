import api.service.connection.connect_motors as connect

class getMotersList():
     CMD = 'for f in /sys/class/tacho-motor/*; do echo $f; done'
     def command(self, sshClient: connect.connectEv3Dev):
          motors = []
          motors = sshClient.send(self.CMD)
          return motors
     

