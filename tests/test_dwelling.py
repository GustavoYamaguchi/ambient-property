import unittest
from ambient_property.dwelling import Dwelling
from ambient_property.hub import Hub

class DwellingTest(unittest.TestCase):
    def test_occupy_vacate(self):
        d = Dwelling("home1")
        self.assertFalse(d._occupied)

        d.occupy()
        self.assertTrue(d._occupied)

        d.vacate()
        self.assertFalse(d._occupied)

    def test_connect_hub_and_list(self):
        d = Dwelling("home2")
        h = Hub("hub1")

        d.connect_hub(h)
        self.assertIn(h, d.hubs)
