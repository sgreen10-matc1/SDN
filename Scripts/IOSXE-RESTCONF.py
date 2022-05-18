import requests
import json
import urllib3
urllib3.disable_warnings() # disables the unsecure request warning

def getInts(deviceIP): # create getInts function with deviceIP as the parameter
    url = "https://" + deviceIP + ":443/restconf/data/ietf-interfaces:interfaces" # defining url variable, concantenating deviceIP


    username = 'cisco' # username to log into the router
    password = 'cisco' # password for the username to log into the router
    payload={}
    headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json',
    'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'
    }

    response = requests.request("GET", url, auth = (username,password), verify = False, headers=headers, data=json.dumps(payload)).json() # returns response.json

    intDict = response["ietf-interfaces:interfaces"]["interface"] # creates intDict from response
    
    return intDict # returns intDict

def printInt(intDict): # creates printInt function with intDict as the parameter
    
    for interfaces in intDict: # for loop iterating through all interfaces in intDict
        
        if interfaces["type"] == "iana-if-type:ethernetCsmacd": # if the interface type is labeled the same as "iana-if-type:ethernetCsmacd", this is to address the loopback address or lack thereof
            ipAddInt = interfaces["ietf-ip:ipv4"]["address"] # creates ipAddInt variable, from intDict, with the IP addresses of each interface
            
            for interface in ipAddInt: # nested for loop iterating through interface in ipAddInt
                ipAdd = interface["ip"] # creates ipAdd variable that assigns the contents ip from intDict
                netMask = interface["netmask"] # creates netMask variable that assigns the contents of netmask from intDict
                print(interfaces["name"] + "\t\t" + ipAdd + "\t" + netMask) # print statement containing information for "name" and the variables ipAdd "IP" and netMask "netmask" of each interface

# Main

deviceIP = '10.10.20.175' # creates deviceIP, the mgmtIP address of the router

intDict = getInts(deviceIP) # gets the interfaces model

printInt(intDict) # iterates the dictionary that was returned
