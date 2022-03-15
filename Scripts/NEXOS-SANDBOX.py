#!/usr/bin/env python3

import requests
import json
import urllib3
urllib3.disable_warnings() # disables the unsecure request warning



"""
Modify these please
"""


switchuser = 'cisco' # entry for the username of the switch
switchpassword = 'cisco' # entry for the password for the username of the switch

url = 'https://10.10.20.178/ins' # url and adding the "https" instead of the (http) for authentication and encryption
myheaders = {'content-type': 'application/json-rpc'}
payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params":{
            "cmd": "show version", # command line parameter show version for the command in the CLI
            "version": 1
        },
        "id": 1
    }
]

response = requests.post(url, data=json.dumps(payload), verify=False, headers=myheaders, auth=(switchuser, switchpassword)).json() # verify set to False

type(response) # is a dictionary
print(response) # printing response to verify where the nested dictionaries are located



print(response["result"]["body"].keys()) # printing .keys() of the dictionaries of result and body

inFaceName = "intf-name" # creating a variable for my hostname (called hostName) instead of literally defining it as "host_name"
print("Your interface name is:  " + response["result"]["body"][inFaceName]) # printing out the statement "your hostname is ----"

memSize = "memory" # creating a variable for my memory size called memSize
print("Your memory size is:  " + str(response["result"]["body"][memSize])) # printing out the statement "your memory size is ------""

memType = "mem_type" # creating a variable for the memory type, called memType
print("Your memory type is:  " + response["result"]["body"][memType]) # printing out the statement "your memory type is -----""

print('Hostname = '+response["result"]["body"][hostName]+'\tMemory = '+str(response["result"]["body"][memSize])+' '+response["result"]["body"][memType])
# printing one long statement with all the keys that were required, the hostname, the memory size, and the memory type, and then formatted in between for sentence


response["result"]["body"]["intf-name"]["proto-state"]["link-state"]["admin-state"]["prefix"]

hostName = "host_name" # creating a variable for my hostname (called hostName) instead of literally defining it as "host_name"
print("Your hostname is:  " + response["result"]["body"][hostName]) # printing out the statement "your hostname is ----"

memSize = "memory" # creating a variable for my memory size called memSize
print("Your memory size is:  " + str(response["result"]["body"][memSize])) # printing out the statement "your memory size is ------""

memType = "mem_type" # creating a variable for the memory type, called memType
print("Your memory type is:  " + response["result"]["body"][memType]) # printing out the statement "your memory type is -----""