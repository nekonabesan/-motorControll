import api.service.connection.connect_ev3_dev as connect

class getSensorsType():
    PATH = 'cat -s /sys/class/lego-sensor/'
    def command(self, connection: connect.connectEv3Dev, sensor_id: str):
        type = str(connection.sendForGet(self.PATH + sensor_id + '/driver_name'))
        return type