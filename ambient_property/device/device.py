from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, device_id, name):
        self._id = device_id
        self._name = name
        self._paired = False

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def paired(self):
        return self._paired

    @paired.setter
    def paired(self, value):
        if not isinstance(value, bool):
            raise ValueError("Paired must be a boolean")
        self._paired = value

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def modify(self, *args, **kwargs):
        pass
