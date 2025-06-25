from ambient_property.device.utils.device_type import DeviceType
from ambient_property.device_manager import DeviceManager
from ambient_property.hub import Hub


def driver():
    manager = DeviceManager()

    print("\n--- Creating Devices ---")
    manager.create_device(DeviceType.SWITCH, "switch1", "Living Room Switch")
    manager.create_device(DeviceType.THERMOSTAT, "thermostat1", "Hall Thermostat")
    manager.create_device(DeviceType.LOCKER, "locker2", "Door Locker")
    manager.create_device(DeviceType.DIMMER, "dimmer2", "Living Room lights")

    print("\n--- Listing Devices ---")
    for device in manager.list_devices():
        print(device)

    print("\n--- Creating Dwellings ---")
    manager.create_dwelling("dwelling1")
    manager.create_dwelling("dwelling2")
    print("Created Dwellings: 'dwelling1', 'dwelling2'")

    print("\n--- Installing Hub 1 ---")
    hub1 = Hub("hub1")
    dwelling1 = manager.dwellings["dwelling1"]
    dwelling1.occupy()
    dwelling1.connect_hub(hub1)
    print("Installed 'hub1' into dwelling 'dwelling1'")
    hub2 = Hub("hub2")
    dwelling2 = manager.dwellings["dwelling2"]
    dwelling2.occupy()
    dwelling2.connect_hub(hub2)
    print("Installed 'hub2' into dwelling 'dwelling2'")

    print("\n--- Pairing Devices ---")
    hub1.pair_device(manager.devices["switch1"])
    hub1.pair_device(manager.devices["thermostat1"])
    print("Paired 'switch1' and 'thermostat1' into 'hub1'")
    hub2.pair_device(manager.devices["locker2"])
    hub2.pair_device(manager.devices["dimmer2"])
    print("Paired 'locker2' and 'dimmer2' into 'hub2'")

    print("\n--- Should fail pairing already paired devices---")
    try:
        hub2.pair_device(manager.devices["switch1"])
    except ValueError as e:
        print(f"Caught an error: {e}")

    print("\n--- Modifying Devices State ---")
    switch1 = manager.devices["switch1"]
    switch1.modify()
    print("Updated switch 'switch1' to ON.")
    thermostat1 = manager.devices["thermostat1"]
    thermostat_value = 70
    thermostat1.modify(thermostat_value)
    print(f"Updated switch 'thermostat1' value to {thermostat_value}.")
    locker2 = manager.devices["locker2"]
    locker2.modify(locked=True)
    print("Updated switch 'locker2' to 'locked'.")
    dimmer2 = manager.devices["dimmer2"]
    dimmer_value = 55
    dimmer2.modify(dimmer_value)
    print(f"Updated switch 'dimmer2' value to {dimmer_value}.")

    print("\n--- Listing Devices ---")
    for device in manager.list_devices():
        print(device)

    print("\n--- Unpairing 'switch1' Device ---")
    hub1.unpair_device("switch1")
    print("'switch1' unpaired from 'hub1'")

    print("\n--- Trying to Delete Unpaired Device ---")
    manager.remove_device("switch1")
    print("Removed 'switch1'")

    print("\n--- Trying to Delete Paired Device ---")
    try:
        manager.remove_device("locker2")
    except ValueError as e:
        print(f"Caught an error: {e}")
        print("Failed to delete 'locker2'")

    print("\n--- Trying to Delete unknown Device ---")
    try:
        manager.remove_device("switch2")
    except ValueError as e:
        print(f"Caught an error: {e}")
        print("Failed to delete 'switch2'")

    print("\n--- Final Device List ---")
    for device in manager.list_devices():
        print(device)

    print("\n--- All Dwellings ---")
    print(manager.list_dwellings())

    print("\n--- All Hubs ---")
    print([[hub.info() for hub in dwelling1.hubs], [hub.info() for hub in dwelling2.hubs]])

if __name__ == '__main__':
    driver()