import api.service.connection.connect_ev3_dev as connect

class SetModes():
    PATH='/sys/class/lego-sensor/'
    # echo "GYRO-G&A" > /sys/class/lego-sensor/sensor0/mode && cat /sys/class/lego-sensor/sensor2/mode
    # echo "GYRO-ANG" > /sys/class/lego-sensor/sensor0/mode && cat /sys/class/lego-sensor/sensor2/mode
    def command(self, connection: connect.connectEv3Dev, sensor_id: str):
        connection.sendForSet('echo "GYRO-CAL" > ' + self.PATH  + sensor_id + '/mode && ' 
                    + 'cat ' + self.PATH + sensor_id + '/mode')
        connection.sendForSet('echo "GYRO-G&A" > ' + self.PATH  + sensor_id + '/mode && ' 
                    + 'cat ' + self.PATH + sensor_id + '/mode')
        return 0