#!/usr/bin/env python3

import requests
import json
import urllib3 # imports urllib3 module
urllib3.disable_warnings() # disables the unsecure request warning

# creates "devices" dictionary
devices = {
    "dist-sw01": {
        "hostname": "dist-sw01",
        "deviceType": "switch",
        "mgmtIP": "10.10.20.177"
        },
    "dist-sw02": {
        "hostname": "dist-sw02",
        "deviceType": "switch",
        "mgmtIP": "10.10.20.178"
        }
}


print("Host" + "\t\t" + "Type" + "\t\t" + "MgmtIP") # printing a formatted header with tabs (indents) for the spacing to line up with objects
print("-"*45) # creating a line of "-"s multiplied by 45 for the bottom border of the seperator

for device in devices.values(): ## This iterates through each device in the "devices" dictionary and prints out each hostname, type, and IP
    print(device["hostname"] + "\t" + device["deviceType"] + "\t\t" + device["mgmtIP"])
    