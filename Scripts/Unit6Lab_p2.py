#!/usr/bin/env python3

import requests # imports requests module
import urllib3 # imports urllib3 module
urllib3.disable_warnings() # disables the unsecure request warning
import json # imports json module


def sendCLI(commandCLI, IP): # creates sendCLI function with objects commandCLI and IP

    switchuser='cisco' # device username
    switchpassword='cisco' # device password for username

    url='https://'+IP+'/ins' # url variable which is the device management ip address (IP)

    myheaders={'content-type':'application/json-rpc'}
    payload=[
      {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
          "cmd": commandCLI, # the command that is sent to the device
          "version": 1
        },
        "id": 1
      }
    ]

    response = requests.post(url,data=json.dumps(payload), verify = False, headers=myheaders,auth=(switchuser,switchpassword)).json() # created response.json
    # verify = False below is to accept untrusted certificate
    
    return response


def displayInfo(deviceInfo): # function prints the devices hostname, memory, memory type, chassis ID, and boot "kick" file

    print("Host" + "\t\t", "Memory" + "\t\t", "Mem Type" + "\t", "Chassis" + "\t\t\t", "Boot File") ## This prints the header objects for the table

    print("-" * 115,sep="") # seperator 'line'

    print(deviceInfo["result"]["body"]["host_name"], "\t", deviceInfo["result"]["body"]["memory"], "\t", deviceInfo["result"]["body"]["mem_type"], 
          "\t\t", deviceInfo["result"]["body"]["chassis_id"], "\t", deviceInfo["result"]["body"]["kick_file_name"])
            # prints out specific device information from deviceInfo dictionary

        
# main

devices = { # creates nested dictionary with two switches and basic information (hostname,deviceType,mgmtIP)
    "dist-sw01" : {
        "hostname" : "dist-sw01",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.177"
        },
    
    "dist-sw02" : {
        "hostname" : "dist-sw02",
        "deviceType" : "switch",
        "mgmtIP" : "10.10.20.178"
        }
    }

   
deviceInfo = sendCLI("show version", "10.10.20.177") # executes sendCLI function with the cmd "show version" and mgmt IP "10.10.20.177"

displayInfo(deviceInfo) # executes printInfo function and returns specific device information from mgmtIP address

print('') # creates blank space between each device's tables

deviceInfo = sendCLI("show version", "10.10.20.178") # executes sendCLI function with the cmd "show version" and mgmt IP "10.10.20.178"

displayInfo(deviceInfo) # executes printInfo function and returns specific device information from mgmtIP address





