import api.service.connection.connect_ev3_dev as connect

class getSpeed():
     def command(self, connection: connect.connectEv3Dev, sensor_id: str):
          speed = connection.sendForGet('cat /sys/class/lego-sensor/' + sensor_id + '/value1')
          return speed