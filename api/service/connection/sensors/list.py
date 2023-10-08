import api.service.connection.connect_motors as connect

class getSensorsList():
     CMD = 'for f in /sys/class/lego-sensor/*; do echo "$f"; done'
     def command(self, connection: connect.connectEv3Dev):
          sensors = []
          sensors = connection.sendForList(self.CMD)
          return sensors