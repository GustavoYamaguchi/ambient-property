from typing import Dict

from ambient_property.device.device import Device


class Hub:
    def __init__(self, hub_id: str):
        self.id = hub_id
        self._paired_devices: Dict[str, Device] = {}

    @property
    def paired_devices(self):
        return self._paired_devices

    def pair_device(self, device: Device):
        if device.paired:
            raise ValueError(f"Device {device.id} is already paired.")
        self._paired_devices[device.id] = device
        device.paired = True

    def unpair_device(self, device_id: str):
        device = self._paired_devices.get(device_id)
        if not device or not device.paired:
            raise ValueError(f"Device {device_id} is not paired.")
        del self._paired_devices[device.id]
        device.paired = False

    def get_device_info(self, device_id: str):
        return self._paired_devices.get(device_id).info()

    def info(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'paired_devices': list(self.paired_devices.keys()),
        }