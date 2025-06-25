from typing import Dict

from ambient_property.device.device import Device

MIN_VALUE = 0
MAX_VALUE = 100


class Dimmer(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._value = MIN_VALUE

    def info(self) -> Dict[str, str]:
        return {
            'device_id': self.id,
            'name': self.name,
            'paired': self.paired,
            'value': self._value,
        }

    def modify(self, value):
        if not (MIN_VALUE <= value <= MAX_VALUE):
            raise ValueError(f"Dimmer value should be in range {MIN_VALUE} - {MAX_VALUE}, got {value}.")
        self._value = value

