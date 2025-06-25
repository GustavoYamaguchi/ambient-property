# Ambient Property

Ambient Property proof-of-concept smart home device manager that models dwellings, hubs, and IoT devices. All 
demonstrated through a simple driver function using in-memory storage.  

### Challenge summary
The Device Manager is a system designed to manage smart IoT devices within a dwelling, supporting operations like 
pairing, updating, and removing devices. It involves key entities: Dwellings, Hubs, and various Devices (Switch, 
Dimmer, Lock, Thermostat). Hubs act as intermediaries to facilitate communication between devices and the system. 
The solution supports creating, modifying, and listing devices, as well as managing hub-device pairings and dwelling 
occupancy states.  

### Features
- Pairing/unpairing devices
- Managing device state 
- Tracking dwelling occupancy

### Driver

Driver function is a script, that tests use-cases and prints its actions. It manages 2 dwellings, 
with different hubs, which devices will pair/unpair and modify their statuses, depending on the device. 


## How to run driver function

```bash
python3 -m ambient_property.driver
```


## How to run tests

```bash
python3 -m unittest discover
```