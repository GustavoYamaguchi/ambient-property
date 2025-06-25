from ambient_property.device.device import Device

MIN_VALUE = 41
MAX_VALUE = 95

class Thermostat(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._value = MIN_VALUE

    def info(self):
        return {
            'device_id': self.id,
            'name': self.name,
            'paired': self.paired,
            'value': self._value,
        }

    def modify(self, value):
        if not (MIN_VALUE <= value <= MAX_VALUE):
            raise ValueError(f"Thermostat value should be in range {MIN_VALUE} - {MAX_VALUE}, got {value}.")
        self._value = value
