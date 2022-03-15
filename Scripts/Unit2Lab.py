#!/usr/bin/env python3

# create router1 dicitionary
router1 = {
    "brand": "Cisco",
    "model": "1941",
    "mgmtIP": "10.0.0.1",
    "G0/0": "10.0.1.1 /24",
    "G0/1": "10.0.2.1 /24",
    "G0/2": "10.0.3.1 /24",
    "hostname": "r1",
}

# assigns 10.0.0.1 to a variable called "ip"
ip = router1["mgmtIP"]

print(ip)
# print ip variable

# print output of keys
print(router1.keys())

# print output of values
print(router1.values())

# print output of combined items keys/values pairs
print(router1.items())

# print output of router1 type
print(type(router1))

# creating x_Values variable that will return a list of all the values
x_Values = router1.values()

# modifying ip address entry for interface G0/2 
router1["G0/2"] = "10.1.3.1 /24"

# printing output of updated values with modified interface ip
print(x_Values)

# modifying entry for model value
router1["model"] = "2901"

# printing output of updated values with modified model value
print(x_Values)

for key, value in router1.items():
    print('key = ' + key + '\t', 'value = ' + value)
    # print the current dictionary (router1) key/value pairs 


validContinue = False # create boolean control variable

while validContinue == False:
    
    add_IP_Input = input("Do you want to change the Management IP address (y or n)? ")
    # create add_IP_Input variable from user input
    
    if add_IP_Input.upper() == "Y":
        validContinue = True # exit while loop
        enterIP = True # set flag for valid IP to enter loop to validate IP
        
    elif add_IP_Input.upper() == "N":
        validContinue = True # exit while loop
        enterIP = False # skip getting IP input
        
    else:
        print("Invalid Entry")

validIP = False

while enterIP == True:
    
    # 1. check to make sure there are only 4 octets
    # 2. check to make sure that those octets are numeric
    # 3. check to make sure that octets are in correct range
    
    enterIP = False
    validIP = True
    
    # create ipString variable and get IP address from user input
    ipString = input("Enter a valid IP address: ")
    
    octets = ipString.split(".")
    if len(octets) == 4: # check to make sure the length is 4, if so, continue on the loop
        
        for octet in octets :
            if octet.isnumeric() == True: # check to make sure user input is numeric
                if int(octet) < 0 or int(octet) >255: # invalid range
                    validIP = False
                    enterIP = True # stay in the loop
                    
            else: # address not numeric
                validIP = False
                enterIP = True # stay in the loop
                
        if enterIP == True: # return message about entering correct number value
            print("Address octets must be numeric and between 0 and 255")
            
    else: # to many octets
        print("Your address must have only four octets x.x.x.x")
        validIP = False
        enterIP = True # stay in the loop

if validIP == True:
    router1["mgmtIP"] = ipString
    # modifying entry for model value
    print("Management IP address, " + ipString + ", was successfully updated!")
    # return message that the Management IP address was successfully updated



for key, value in router1.items():
    print('key = ' + key + '\t', 'value = ' + value )
    # print out the updated dictionary with new mgmtIP address included