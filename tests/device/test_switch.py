import unittest
from ambient_property.device.switch import Switch

class TestDevices(unittest.TestCase):
    def test_switch(self):
        s = Switch("s1", "Wall Switch")
        self.assertEqual(s.id, "s1")
        self.assertFalse(s.paired)

        self.assertFalse(s.info()['on'])
        s.modify()
        self.assertTrue(s.info()['on'])
