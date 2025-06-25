import unittest
from ambient_property.hub import Hub

class DummyDevice:
    def __init__(self, device_id):
        self.id = device_id
        self.paired = False

    def info(self):
        return {"id": self.id, "paired": self.paired}

class HubTest(unittest.TestCase):
    def test_pair_and_unpair_device(self):
        hub = Hub("hub1")
        device = DummyDevice("dev1")
        hub.pair_device(device)
        self.assertIn("dev1", hub.paired_devices)
        self.assertTrue(device.paired)

        hub.unpair_device("dev1")
        self.assertNotIn("dev1", hub.paired_devices)
        self.assertFalse(device.paired)

    def test_pair_already_paired_device(self):
        hub = Hub("hub1")
        device = DummyDevice("dev1")
        device.paired = True
        with self.assertRaises(ValueError):
            hub.pair_device(device)

    def test_unpair_nonexistent_device(self):
        hub = Hub("hub1")
        with self.assertRaises(ValueError):
            hub.unpair_device("dev1")
