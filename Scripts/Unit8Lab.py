import requests
import json
import urllib3
urllib3.disable_warnings() # disables the unsecure request warning
import re # import regular expression

def validateIP(IPString): # create validateIP function with IPString parameter
    validIP = True # establishing validIP starting position to "True"
    octets = IPString.split(".") # octets variable created with switchString.split with "period" delimeter
    if len(octets) != 4: # if length of "octets" variable is not "4" (seperated with the ".") then validIP
        validIP = False  # continues onto next part of loop
    else: # check numbers
        for octet in octets : # if each set of elements spaced between "." delimeter"
            if octet.isnumeric() == True: # "check" making sure its a number, if it is a number then "check" to see if
                if int(octet) < 0 or int(octet) >255: # less than "0" or higher than "255"
                    validIP = False # if less than 0 or higher than 255, validIP value changes to "False"
            else:
                validIP = False # otherwise value is set to False
    return validIP # returns the value of validIP

def validateHost(hostname): # create the validateHost function with hostname as the parameter
    validHost = True # establishing validHost starting position to "True"
    spaces = hostname.split() # creating spaces variable from "hostname" split, () default delimeter is "element spaced", basically a "space/whitespace"
    spaces1 = str(hostname) # creating spaces1 variable from string converted data type of "hostname"
    if len(spaces) == False: # if length of "spaces" variable is greater than 1 (seperated with "any "space" between "elements" ")
        validHost = False # then validHost remains at False value and continues on in the loop
    else:
        if spaces1.isalpha() == False: # if spaces1 string variable doesnt start with alphanumeric character
            validHost = False # validHost value would still remain at a "False" value   
    validHostCheck = re.compile('[@_!#$%^&*()<>?/\|}{~:.,]') # created validHostCheck, will not accept any of the following characters using regular expression
    if(validHostCheck.search(hostname) == None): # if searching through hostname did not find any of the characters from validHostCheck
        validHost = True # validHost value is changed to True
    else:
        validHost = False # otherwise the value is set to False
    return validHost # returns the value of validHost

def getCookie(addr) : # create the getCookie function with addr as the parameter
    
#NX REST API Authen See REST API Reference for format of payload below

    url = "https://"+ addr + "/api/aaaLogin.json" # concantenating addr variable, which is the mgmt ip address of the switch
 
    payload= {"aaaUser" : # payload contains username and password to log into the switch
              {"attributes" :
                   {"name" : "cisco",
                    "pwd" : "cisco"}
               }
          }

    response = requests.post(url, json=payload, verify = False)
    
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"] # returns response.json

def newHostname(switchIP,changeHost): # creates newHostname function with parameters switchIP and changeHost
    cookie = getCookie(switchIP) # defining cookie variable from getCookie function with parameter switchIP
    url = "https://"+switchIP+"/api/node/mo/sys.json?query-target=self" # defining url variable, concantenating switchIP

    payload= { # payload of changeHost, which will be the variable to update with new switch hostname
        "topSystem" :
                {"attributes" :
                    {"name" : changeHost
                     
                } # type attribute
            }
        }
    
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + cookie # concatenating APIC-cookie with cookie value from getCookie function
}

    response = requests.request("POST", url, headers=headers, verify = False, data=json.dumps(payload)) # POST response, json.dumps with (payload)

    return response

# Main

switchName = input("Enter Switch Hostname: ") # asking for user input for switch to modify, storing that as switchName

if validateHost(switchName) == True:
    switchIP = input("Enter Switch Management IP Address: ") # asking for user input for the mgmtIP address to modify, storing that as switchIP
    
    if validateIP(switchIP) == True:
        changeHost = input("Enter New Switch Hostname: ") # asking for user input for the new hostname of the switch, storing that as changeHost
        
        if validateHost(changeHost) == True:
            newHostname(switchIP, changeHost)
            print("Switch Hostname Successfully Changed!") # print message informing user that switch hostname was successfully changed
            
        else:
            print("Invalid Hostname Entered, Please Try Again.") # print message informing user that invalid hostname was entered
            
    else:
        print("Invalid IP Address Entered, Please Try Again.") # print message informing user that invalid IP address was entered
        
else:
    print("Invalid HostName Entered, Please Try Again.") # print message informing user that invalid hostname was entered