#!/usr/bin/env python3

def getInput(prompt,validationList): # create getInput function
    answer = input(prompt) # gets user input, creating answer variable
    while answer not in validationList: # if answer not on the approved validationList, print comment of whats acceptable input, try again
        print("The following are valid inputs" + str(validationList)) 
        answer = input(prompt)    
    return answer

def printDevices(devices): # create printDevices function
    for device in devices.keys(): # getting "device" keys from devices dictionary, then printing it out to screen for user
        print(devices[device] ["hostname"] + "\t\t\t " + devices[device] ["mgmtIP"] + "\t\t" + devices[device] ["type"] + "\t\t")

def GetDeviceInfo(): # create GetDeviceInfo function and get device information for new device, (type/hostname/ip)
    returnDict = {"type": "",
            "hostname": "",
            "mgmtIP": ""
            }
    returnDict["hostname"] = input("Enter hostname: ")
    returnDict["mgmtIP"] = input("Enter IP: ")
    return returnDict # return that as returnDict dictionary type

def validateIP(ipString): # create validateIP function
    validIP = True # establishing validIP starting position to "True"
    octets = ipString.split(".") # octets variable created with ipString.split with "period" delimeter
    if len(octets) != 4: # if length of "octets" variable is not "4" (seperated with the ".") then validIP
        validIP = False  # continues onto next part of loop
    else: # check numbers
        for octet in octets : # if each set of elements spaced between "." delimeter"
            if octet.isnumeric() == True: # "check" making sure its a number, if it is a number then "check" to see if
                if int(octet) < 0 or int(octet) >255: # less than "0" or higher than "255"
                    validIP = False # if less than 0 or higher than 255, validIP value changes to "False"
            else:
                validIP = False
    return validIP # will return validIP as a "True" value if it passed being a number and within the correct range.

def validateHost(hostname): # create the validateHost function
    validHost = True # establishing validHost starting position to "True"
    spaces = hostname.split() # creating spaces variable from "hostname" split, () default delimeter is "element spaced", basically a "space/whitespace"
    spaces1 = str(hostname) # creating spaces1 variable from string converted data type of "hostname"
    if len(spaces) == False: # if length of "spaces" variable is greater than 1 (seperated with "any "space" between "elements" ")
        # there is obviously a few mistakes here, and i am still learning, i think the greater lesson is that i know something is incorrect with the logic
        validHost = False # then validHost remains at False value and continues on the loop
    else:
        if spaces1.isalpha() == False: # if spaces1 string variable doesnt start with alphanumeric character
            validHost = False # validHost value would still remain at a "False" value
    return validHost # returns a "True" value (which is what was defined at the start) for the "validateHost" function

def updateDictionary(deviceDict, devices): # create the updateDictionary function with the user input that was gathered from GetDeviceInfo fuction
    hostname = deviceDict["hostname"]
    devices[hostname] = deviceDict

# creates "devices" dictionary
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

printDevices(devices) # print devices from "devices" dictionary

addDevice = getInput("Do you want to add a new device? (y/n)" , ["y", "n", "Y", "N"]) # asking for user input on whether to add new device, either (y or n)

if addDevice.lower() == "y" : # starting the validation "check" statements, "yes" will continue going further in the loop
    validDevice = False # creating validDevice control variable & setting value to "false", if "check" statents pass, then will change to "true", otherwise remains "false"
    while validDevice == False: # next "check" statement for validDevice
        
        deviceType = getInput("Is this device going to be a switch or a router? (Enter either s or r) ", ["s", "S", "r", "R"]) # asking for user input, either (s/S or r/R)
        deviceDict = GetDeviceInfo() # user input for (hostname/IP) & returns dictionary in devices format
        
        validIP = validateIP(deviceDict["mgmtIP"]) # receives a string "IP addr" & returns Boolean "true" for valid IP & "false" for invalid IP
        
        validHost = validateHost(deviceDict["hostname"]) # receives a string "hostname" & returns Boolean "true" for valid host & "false" for invalid host
        
        if deviceType.lower() == "s" : # check statement to verify either switch or router, from earlier user input, then adding and updating the dictionary
            deviceDict["type"] = "switch"
        else:
            deviceDict["type"] = "router"
        
        if validIP == True and validHost == True: # if validIP and validHost "checks" pass, then "validDevice" variable is changed to "true"
            validDevice = True
            
        if validIP == False: # if validIP "check" statement is false, print the following message
            print("Bad IP address, please try again")
        
        if validHost == False: # if validHost "check" statement is false, print the following message
            print("Bad hostname, please try again")
    
    updateDictionary(deviceDict, devices) # update dictionary with new device information
    print("Device Successfully Added!! \n \t \n Refreshing Device List... \n") # print message informing user that device was added, then print out the updated dictionary
    printDevices(devices)
    
else: # if user doesn't add device, print the following message
    print("Adding new device failed, nothing updated!")