class Sensor:

    _sensor_name = None
    _sensor_type = None

    def __init__(self, sensor_name, sensor_type):
        self._sensor_name = sensor_name
        self._sensor_type = sensor_type

    def get_sensor_name(self):
        print(self._sensor_name)
    
    def set_sensor_name(self, name):
        self._sensor_name = name

    def get_sensor_type(self):
        print(self._sensor_type)

    def set_sensor_type(self, sensor_type):
        self._sensor_type = sensor_type

# if __name__ == "__main__":
#     import sys
#     Sensor(int(sys.argv[1]))