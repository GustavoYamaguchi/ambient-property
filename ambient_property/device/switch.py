from typing import Dict

from ambient_property.device.device import Device


class Switch(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._on = False

    def info(self) -> Dict[str, str]:
        return {
            'device_id': self.id,
            'name': self.name,
            'paired': self.paired,
            'on': self._on,
        }

    def modify(self) -> None:
        self._on = not self._on