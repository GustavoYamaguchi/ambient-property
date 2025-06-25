from typing import Dict

from ambient_property.device.device import Device
from ambient_property.device.utils.device_type import DeviceType
from ambient_property.dwelling import Dwelling


class DeviceManager:
    def __init__(self):
        self.devices: Dict[str, Device] = {}
        self.dwellings: Dict[str, Dwelling] = {}

    def create_device(self, device_type: DeviceType, device_id: str, name: str) -> Device:
        if device_id in self.devices:
            raise ValueError(f"Id should be unique, {device_id} already exists.")
        device_class = DeviceType.map_to_class(device_type)
        device = device_class(device_id, name)
        self.devices[device.id] = device
        return device

    def remove_device(self, device_id: str) -> None:
        device = self.devices.get(device_id)
        if not device:
            raise ValueError(f"Unknown device {device_id}.")
        if device.paired:
            raise ValueError(f"Device {device_id} should be unpaired, before removing it.")

        del self.devices[device_id]

    def list_devices(self):
        return [device.info() for device in self.devices.values()]

    def create_dwelling(self, dwelling_id) -> Dwelling:
        if dwelling_id in self.dwellings:
            raise ValueError(f"Id should be unique, {dwelling_id} already exists.")
        self.dwellings[dwelling_id] = Dwelling(dwelling_id)
        return self.dwellings[dwelling_id]

    def list_dwellings(self):
        return list(self.dwellings.keys())