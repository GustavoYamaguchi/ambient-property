import unittest

from ambient_property.device.thermostat import Thermostat, MIN_VALUE, MAX_VALUE


class TestThermostat(unittest.TestCase):
    def setUp(self):
        self.thermostat = Thermostat(id=101, name="Bedroom Thermostat")

    def test_initialization(self):
        self.assertEqual(self.thermostat.id, 101)
        self.assertEqual(self.thermostat.name, "Bedroom Thermostat")
        self.assertEqual(self.thermostat.info()['value'], MIN_VALUE)

    def test_info_method(self):
        self.thermostat.paired = False
        expected = {
            'device_id': 101,
            'name': "Bedroom Thermostat",
            'paired': False,
            'value': MIN_VALUE,
        }
        self.assertEqual(self.thermostat.info(), expected)

    def test_modify_valid_values(self):
        for temp in [41, 50, 72, 95]:
            with self.subTest(value=temp):
                self.thermostat.modify(temp)
                self.assertEqual(self.thermostat.info()['value'], temp)

    def test_modify_below_minimum(self):
        with self.assertRaises(ValueError) as context:
            self.thermostat.modify(MIN_VALUE - 1)
        self.assertIn("Thermostat value should be in range", str(context.exception))

    def test_modify_above_maximum(self):
        with self.assertRaises(ValueError) as context:
            self.thermostat.modify(MAX_VALUE + 1)
        self.assertIn("Thermostat value should be in range", str(context.exception))

    def test_modify_at_bounds(self):
        self.thermostat.modify(MIN_VALUE)
        self.assertEqual(self.thermostat.info()['value'], MIN_VALUE)

        self.thermostat.modify(MAX_VALUE)
        self.assertEqual(self.thermostat.info()['value'], MAX_VALUE)

