import api.service.connection.connect_motors as connect

class getSpeed():
     def command(self, connection: connect.connectEv3Dev, sensor_id: str):
          pwm_value = connection.sendForGet('cat /sys/class/lego-sensor/' + sensor_id + '/value1')
          return pwm_value