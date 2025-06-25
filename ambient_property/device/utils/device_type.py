from enum import Enum
from typing import Dict, Type

from ambient_property.device.device import Device
from ambient_property.device.dimmer import Dimmer
from ambient_property.device.locker import Locker
from ambient_property.device.switch import Switch
from ambient_property.device.thermostat import Thermostat


class DeviceType(Enum):
    SWITCH = 1
    DIMMER = 2
    LOCKER = 3
    THERMOSTAT = 4

    @staticmethod
    def map_to_class(device_type: 'DeviceType') -> Type[Device]:
        return _device_map[device_type]


_device_map: Dict['DeviceType', Type[Device]] = {
    DeviceType.SWITCH: Switch,
    DeviceType.DIMMER: Dimmer,
    DeviceType.LOCKER: Locker,
    DeviceType.THERMOSTAT: Thermostat,
}

