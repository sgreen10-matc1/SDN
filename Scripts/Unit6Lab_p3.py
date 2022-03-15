#!/usr/bin/env python3

import requests # imports requests module
import urllib3 # imports urllib3 module
urllib3.disable_warnings() # disables the unsecure request warning
import json # imports json module


def getOSPFNeighbor(commandCLI, IP): # creates getOSPFNeighbor function with objects commandCLI and IP

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


def printOSPFNeighbor(OSPF_Neighbor): # creates printOSPFNeighbor with the object of OSPF_Neigbor

    print("Router-ID" + "\t\t", "Neighbor IP" + "\t\t", "Int") # creates header objects for the table

    print("-" * 60, sep="") # creates the formatting for the table/seperator

    neighList = OSPF_Neighbor["result"]["body"]["TABLE_ctx"]["ROW_ctx"]["TABLE_nbr"]["ROW_nbr"] # creates variable from the contents of OSPF_Neighbor dictionary

    for neigh in neighList: # for item in items
        print(neigh["rid"] + "\t\t", neigh["addr"] + "\t\t", neigh["intf"]) 
        # iterates through the neighList item and prints out each item
        
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

for device in devices.values(): # for loop displaying devices dictionary values

    mgmtIP = device["mgmtIP"] # creates mgmtIP variable and assigns each device management ip address to it

    print(device["hostname"], "OSPF Neighbors") # prints out each device name "hostname" and adds OSPF Neighbors after
    
    OSPF_Neighbor = getOSPFNeighbor("show ip ospf neighbor", mgmtIP) 
    # executes getOSPFNeighbor function with the cmd from (commandCLI) "show ip ospf neighbor" for each mgmtIP from the devicesDict dictionary

    printOSPFNeighbor(OSPF_Neighbor) # executes printOSPFNeighbor function with OSPF_Neighbor has an object and returns the information

    print('') # creates blank space between each device's tables


