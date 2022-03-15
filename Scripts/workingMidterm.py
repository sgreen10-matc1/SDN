#!/usr/bin/env python3

import requests
import json
import urllib3
urllib3.disable_warnings() # disables the unsecure request warning

def sendCLI(commandCLI, IP): # create sendCLI function with commandCLI and IP address as object parameters defined

  switchuser = 'cisco' # entry for the username of the switch
  switchpassword = 'cisco' # entry for the password for the username of the switch

  url = 'https://'+IP+'/ins' # url variable with the ip address (IP) variable concantenated in between the https and ins
  myheaders = {'content-type': 'application/json-rpc'}
  payload = [
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": commandCLI, # commandCLI variable, can be used as a universal command variable for sending anything to CLI
            "version": 1
        },
        "id": 1
    }
  ]

  response = requests.post(url, data=json.dumps(payload), verify=False, headers=myheaders, auth=(switchuser, switchpassword)).json() # created response.json
  someDict = response["result"]["body"]["TABLE_intf"]["ROW_intf"] # reassign response to someDict
  return someDict # return someDict.json request

def update(intName, newIpAdd, value): # creates update function with interface name 'intName', IP address, and newIpAdd as the object parameters defined

  switchuser='cisco' # entry for the username of the switch
  switchpassword='cisco' # entry for the password for the username of the switch

  url='https://'+value+'/ins' # url variable with the ip address (IP) variable concantenated in between the https and ins
  myheaders={'content-type':'application/json-rpc'}
  payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "configure terminal",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "interface "+intName, # intName variable concantenated with "interface", command goes into each vlan interface
      "version": 1
    },
    "id": 2 # id value +1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip address " +newIpAdd+ " 255.255.255.0", # newIpAdd variable concantenated between "ip address" and subnet "255.255.255.0", command puts in new IP address
      "version": 1
    },
    "id": 3 # id value +1
  }
]

  response = requests.post(url, data=json.dumps(payload), verify=False, headers=myheaders, auth=(switchuser, switchpassword)).json() # created response.json
  return response # return response.json

def dictInt(someDict): # create dictInt function with someDict as the object parameter defined
  displayOut = "" # creates temp placeholder, currently isn't defined as anything, other variables linking to it, "using it", reference when code is read in sequence
  print(f"Name:\tProto:\tLink:\tAddress:") # printing a formatted header with 3 tabs (indents) for the spacing to line up with displayOut
  print("="*40) # creating a line of "="s multiplied by 40 for the bottom border of the header
  
  for interfaces in someDict: # for loop iterating through all interfaces in someDict
    intName = interfaces['intf-name'] # creates intName variable that assigns the contents of intf-name from someDict
    proState = interfaces['proto-state'] # creates proState variable that assigns the contents of proto-state from someDict
    linState = interfaces['link-state'] # creates linState variable that assigns the contents of link-state from someDict
    ipAdd = interfaces['prefix'] # creates ipAdd variable that assigns the contents of prefix from someDict
    print(intName+'\t'+proState+'\t'+linState+'\t'+ipAdd) #print statement with the newly created variables and 3 tabs in between each to format the output
    
    displayOut += f"{intName}\t{proState}\t{linState}\t{ipAdd}\n" # displayOut a variable of a formatted intName, proState, linState, and ipAdd with 3 tabs and 1 new line
  return displayOut # return the displayOut variable

def addNewIP(ipAdd, octet, octetPosition): # creates addNewIP function with interface IP address, octet, and octet position parameters defined
  octetAdjNumb = octet - 1 # adjusts for python numbering system and corrects it by subtracting 1 from octet, step 1 (ex. 1,2,3 translates to 0,1,2)
  octets = ipAdd.split(".") # creates octets variable from ipAdd.split with period "." character as the identified delimiter value, this totals to "4" octets, step 2
  octetCombPosition = int(octets[octetAdjNumb]) + octetPosition # combines first 2 steps by associating the fixed position and how many octets were created, step 3
  octetStrType = str(octetCombPosition) # creates octetStrType variable by converting octetCombPosition to a string data type, step 4
  octets[octetAdjNumb] = octetStrType # combines step 1 and 2 to step 3, puts together (octets spacing created) with (adjusted fixed position) to (octetStrType string)
  newIpAdd = octets[0] + "." + octets[1] + "." + octets[2] + "." + octets[3] # defines newIpAdd variable, created from, octets + "."" character as delimiter
  return newIpAdd # returns newIpAdd to be called later for main script portion

# main

devices = { # creates the devices dictionary with both switches, (hostname = key, mgmt IP address = value)
  'dist-sw01': '10.10.20.177',
  'dist-sw02': '10.10.20.178'
  }

for key, value in devices.items(): # for loop iterating through devices.items, hostname/mgmtIP will be "key/value" pairs defined
  someDict = sendCLI("show ip interface brief", value) # re-assigns someDict from sendCLI function with show ip interface brief command and device mgmt IP value
  print('hostname = '+key+'\n'+'mgmt IP = '+value) # prints hostname/mgmtIP address before interface info, allows for proper indentification of devices
  dictInt(someDict) # calling dictInt function with parameters "someDict", sends/receives show ip interface brief command
  print('') # creating some empty space
  
  updateList = sendCLI("show ip interface brief", value) # creates updateList from sendCLI function with show ip interface brief command/mgmt IP value of device(s)
  for interface in updateList: # for loop, interating through each interface in updateList
        intName = interface['intf-name'] # creates intName variable that assigns the contents of intf-name from updateList
        ipAdd = interface['prefix'] # creates ipAdd variable that assigns the contents of prefix from updateList
        
        if intName.startswith('V' or 'v'): # if intName starts with "V", either upper or lower case value of the letter
          newIpAdd = addNewIP(ipAdd, 4, 5) # creates newIpAdd function from addNewIP function, changing each vlan IP address by adding 5 to the last octet (fourth position)
          update(intName, newIpAdd, value) # calling update function with parameters "interface name, new IP address, mgmt IP address", sends config changes to devices
          
        else: # else statement if didn't match specified criteria -
          pass # this will help make sure the non vlan interface IP addresses will be unmodified

  finalList = sendCLI("show ip interface brief", value) # creates finalList from sendCLI function with show ip interface brief command/mgmt IP value of device(s)    
  print("Successfully updated VLAN IP Addresses!") # print statement, notifying user that vlan IP address interfaces were successfully updated
  dictInt(finalList) # calling dictInt function with parameters "finalList", sends/receives the last show ip interface brief command
  print('') # creating some empty space