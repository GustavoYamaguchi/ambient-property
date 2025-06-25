from abc import ABC

from ambient_property.hub import Hub


class Dwelling(ABC):
    def __init__(self, structure_id):
        self._id = structure_id
        self._occupied = False
        self._hubs = set()

    def connect_hub(self, hub: Hub) -> None:
        self._hubs.add(hub)

    @property
    def hubs(self):
        return self._hubs

    def occupy(self) -> None:
        self._occupied = True

    def vacate(self) -> None:
        self._occupied = False

