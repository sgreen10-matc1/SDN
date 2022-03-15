#!/usr/bin/env python3

# creating router1 dictionary
router1 = {
        "hostname": "R1",
        "brand": "Cisco",
        "mgmtIP": "10.0.0.1",
        "interfaces": {
            "G0/0": "10.1.1.1",
            "G0/1": "10.1.2.1"
            }
}

# printing keys for router1 and interfaces dictionaries
print(router1.keys())
print(router1["interfaces"].keys())

# printing values for router1 and interfaces dictionaries
print(router1.values())
print(router1["interfaces"].values())

# printing items for router1 and interfaces dictionaries
print(router1.items())
print(router1["interfaces"].items())

# creating myFamily dictionary
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
        },
    "child2": {
        "name": "Tobias",
        "year": 2007
        },
    "child3": {
        "name": "Linus",
        "year": 2011
        }
}

# printing "name" from child2 nested dictionary within "myFamily" dictionary
print(myFamily["child2"]["name"])

# creating "devices" dictionary
devices = {
    "R1": {
        "type": "router",
        "hostname": "R1",
        "mgmtIP": "10.0.0.1"
        },
    "R2": {
        "type": "router",
        "hostname": "R2",
        "mgmtIP": "10.0.0.2"
        },
    "S1": {
        "type": "switch",
        "hostname": "S1",
        "mgmtIP": "10.0.0.3"
        },
    "S2": {
        "type": "switch",
        "hostname": "S2",
        "mgmtIP": "10.0.0.4"
        }
}

# printing "devices" dictionary
print(devices)

# create "for" loop - iterates through "devices" dictionary printing out "ping str" and "mgmtIP" keys from all devices
for device in devices.keys():
    print("ping" + " " + devices[device] ["mgmtIP"])