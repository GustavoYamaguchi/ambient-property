import unittest
from unittest.mock import patch

from ambient_property.device_manager import DeviceManager
from ambient_property.device.utils.device_type import DeviceType

# class DummyDeviceType:
#     @staticmethod
#     def map_to_class(device_type):
#         class DummyDevice:
#             def __init__(self, id, name):
#                 self.id = id
#                 self.name = name
#                 self.paired = False
#
#             def info(self):
#                 return {"id": self.id, "name": self.name, "paired": self.paired}
#         return DummyDevice

class DummyDevice:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.paired = False

    def info(self):
        return {"id": self.id, "name": self.name, "paired": self.paired}

# DeviceType.map_to_class = DummyDeviceType.map_to_class
def dummy_map_to_class(device_type):
    return DummyDevice


@patch('ambient_property.device.utils.device_type.DeviceType.map_to_class', side_effect=dummy_map_to_class)
class DeviceManagerTest(unittest.TestCase):
    def test_create_and_list_devices(self, _):
        dm = DeviceManager()
        dm.create_device(DeviceType.SWITCH, "dev1", "TestDevice")
        self.assertEqual(len(dm.list_devices()), 1)

    def test_remove_device(self, _):
        dm = DeviceManager()
        device = dm.create_device(DeviceType.SWITCH, "dev2", "TestDevice")
        dm.remove_device("dev2")
        self.assertEqual(len(dm.list_devices()), 0)

    def test_remove_paired_device_raises(self, _):
        dm = DeviceManager()
        device = dm.create_device(DeviceType.SWITCH, "dev3", "TestDevice")
        device.paired = True
        with self.assertRaises(ValueError):
            dm.remove_device("dev3")

    def test_create_and_list_dwellings(self, _):
        dm = DeviceManager()
        dm.create_dwelling("dw1")
        self.assertIn("dw1", dm.list_dwellings())
