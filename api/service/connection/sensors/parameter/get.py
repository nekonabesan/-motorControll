import api.service.connection.connect_motors as connect

class Get():
    #cat /sys/class/lego-sensor/sensor1/value0
    #cat /sys/class/lego-sensor/sensor1/value1
    #cat /sys/class/tacho-motor/motor0/speed
    #cat /sys/class/tacho-motor/motor1/speed
    #cat /sys/class/tacho-motor/motor0/position
    #cat /sys/class/tacho-motor/motor1/position
     def command(self, connection: connect.connectEv3Dev, sensor_id: str, motor_a_id: str, motor_b_id: str):
        gyro_angle = int(connection.sendForGet('cat /sys/class/lego-sensor/' + sensor_id + '/value0'))
        gyro_dps = int(connection.sendForGet('cat /sys/class/lego-sensor/' + sensor_id + '/value1'))
        #motor_a_dps = int(connection.sendForGet('cat /sys/class/tacho-motor/' + motor_a_id + '/speed'))
        #motor_b_dps = int(connection.sendForGet('cat /sys/class/tacho-motor/' + motor_b_id + '/speed'))
        #motor_a_position = int(connection.sendForGet('cat /sys/class/tacho-motor/' + motor_a_id + '/position'))
        #motor_b_position = int(connection.sendForGet('cat /sys/class/tacho-motor/' + motor_b_id + '/position'))
        #return gyro_angle,gyro_dps,motor_a_dps,motor_b_dps,motor_a_position,motor_b_position
        return gyro_angle,gyro_dps,0,0,0,0
        