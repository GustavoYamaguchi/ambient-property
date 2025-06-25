import unittest

from ambient_property.device.dimmer import Dimmer, MIN_VALUE, MAX_VALUE


class TestDimmer(unittest.TestCase):
    def setUp(self):
        self.dimmer = Dimmer(id=1, name="Living Room Dimmer")

    def test_initialization(self):
        self.assertEqual(self.dimmer.id, 1)
        self.assertEqual(self.dimmer.name, "Living Room Dimmer")
        self.assertEqual(self.dimmer.info()['value'], MIN_VALUE)

    def test_info_method(self):
        self.dimmer.paired = True
        expected_info = {
            'device_id': 1,
            'name': "Living Room Dimmer",
            'paired': True,
            'value': MIN_VALUE,
        }
        self.assertEqual(self.dimmer.info(), expected_info)

    def test_modify_within_range(self):
        for value in [0, 25, 50, 75, 100]:
            with self.subTest(value=value):
                self.dimmer.modify(value)
                self.assertEqual(self.dimmer.info()['value'], value)

    def test_modify_below_minimum(self):
        with self.assertRaises(ValueError) as context:
            self.dimmer.modify(MIN_VALUE - 1)
        self.assertIn(f"Dimmer value should be in range", str(context.exception))

    def test_modify_above_maximum(self):
        with self.assertRaises(ValueError) as context:
            self.dimmer.modify(MAX_VALUE + 1)
        self.assertIn(f"Dimmer value should be in range", str(context.exception))

    def test_modify_at_bounds(self):
        self.dimmer.modify(MIN_VALUE)
        self.assertEqual(self.dimmer.info()['value'], MIN_VALUE)
        self.dimmer.modify(MAX_VALUE)
        self.assertEqual(self.dimmer.info()['value'], MAX_VALUE)
