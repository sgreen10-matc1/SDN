#!/usr/bin/env python3

import requests
import json
import urllib3
urllib3.disable_warnings() # disables the unsecure request warning

"""
Be sure to run feature nxapi first on Nexus Switch

"""
def sendCLI(commandCLI, IP): # create the sendCLI function with objects commandCLI and IP

  switchuser = 'cisco' # entry for the username of the switch
  switchpassword = 'cisco' # entry for the password for the username of the switch

  url = 'https://'+IP+'/ins' # url variable with the ip address (IP) variable concantenated in between the https and ins
  myheaders = {'content-type': 'application/json-rpc'}
  payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": commandCLI, # command line parameter of "params", this also has the command line command (commandCLI) variable
            "version": 1
        },
        "id": 1
    }
]

  response = requests.post(url, data=json.dumps(payload), verify=False, headers=myheaders, auth=(switchuser, switchpassword)).json() # created response.json

  return response # return response json request, type is dictionary if called
'''
verify=False below is to accept untrusted certificate
'''


def dictInt(intDict): # create dictInt function with an object of intDict

  displayOut = ""
  
  for interfaces in intDict["result"]["body"]["TABLE_intf"]["ROW_intf"]: # for loop displaying the contents in result, body, TABLE_intf, and ROW_intf
    intName = interfaces['intf-name'] # variable that equals the contents of prefix interfaces
    proState = interfaces['proto-state'] # variable that equals the contents of prefix interfaces
    linState = interfaces['link-state'] # variable that equals the contents of prefix interfaces
    ipAdd = interfaces['prefix'] # ipAdd variable that equals the contents of prefix interfaces
    
    displayOut += f"{intName}\t{proState}\t{linState}\t{ipAdd}\n" # displayOut a variable of a formatted intName, proState, linState, and ipAdd with 3 tabs and 1 new line
    
  return displayOut # return the displayOut variable

dictIntFace = sendCLI("show ip interface brief", "10.10.20.177") # creating dictIntFace variable from the sendCLI function with the show ip interface brief command and an IP address 10.10.20.177

interfaces = dictInt(dictIntFace) # creating interfaces variable from dictInt function with dictIntFace as an object

print(f"Name:\tProto:\tLink:\tAddress:") # printing a formatted header with 3 tabs (indents) for the spacing to line up with displayOut
print("-"*36) # creating a line of "-"s multiplied by 36 for the bottom border of the header
print(interfaces) # print the contents of interfaces as the last step


print('\n')

dictIntFace = sendCLI("show ip interface brief", "10.10.20.178") # creating dictIntFace variable from the sendCLI function with the show ip interface brief command and an IP address 10.10.20.177

interfaces = dictInt(dictIntFace) # creating interfaces variable from dictInt function with dictIntFace as an object

print(f"Name:\tProto:\tLink:\tAddress:") # printing a formatted header with 3 tabs (indents) for the spacing to line up with displayOut
print("-"*36) # creating a line of "-"s multiplied by 36 for the bottom border of the header
print(interfaces) # print the contents of interfaces as the last step