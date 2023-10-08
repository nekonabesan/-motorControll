import api.service.connection.connect_motors as connect

class getSensorsType():
    def command(self, connection: connect.connectEv3Dev, sensor_id: str):
        type = connection.sendForValue('tr -d "\n" < /sys/class/lego-sensor/' + sensor_id + '/driver_name')
        return type