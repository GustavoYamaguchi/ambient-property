import unittest

from ambient_property.device.device import Device
from ambient_property.device.dimmer import Dimmer
from ambient_property.device.locker import Locker
from ambient_property.device.switch import Switch
from ambient_property.device.thermostat import Thermostat
from ambient_property.device.utils.device_type import DeviceType


class DeviceTypeTest(unittest.TestCase):
    def test_correct_class(self):
        self.assertEqual(DeviceType.map_to_class(DeviceType.SWITCH), Switch)
        self.assertEqual(DeviceType.map_to_class(DeviceType.DIMMER), Dimmer)
        self.assertEqual(DeviceType.map_to_class(DeviceType.LOCKER), Locker)
        self.assertEqual(DeviceType.map_to_class(DeviceType.THERMOSTAT), Thermostat)

    def test_cover_all_types(self):
        for t in DeviceType:
            self.assertTrue(issubclass(DeviceType.map_to_class(t), Device))
