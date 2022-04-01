import requests
import json
import urllib3
urllib3.disable_warnings() # disables the unsecure request warning

def getCookie(addr) : # create the getCookie function with addr as the parameter
#NX REST API Authen See REST API Reference for format of payload below

    url = "https://"+ addr + "/api/aaaLogin.json" # concantenating addr variable, which is the mgmtIP address of the switch
 
    payload= {"aaaUser" : # payload contains username and password to log into the switch
              {"attributes" :
                   {"name" : "cisco",
                    "pwd" : "cisco"}
               }
          }

    response = requests.post(url, json=payload, verify = False)
    return response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"] # returns response.json

def switchFunc(switchIP): # creates switchFunc function with switchIP as the parameter
    cookie = getCookie(switchIP) # defining cookie variable from getCookie function with parameter switchIP
    url = "https://"+switchIP+"/api/node/mo/sys/ipv4/inst/dom-default.json?query-target=children" # defining url variable, concantenating switchIP

    payload = {
    } # empty payload
    
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + cookie # concatenating APIC-cookie with cookie value from getCookie function
}
    response = requests.request("GET", url, headers=headers, verify = False, data=json.dumps(payload)) # GET response, json.dumps with (payload)
    return response

# Main

switchIP = '10.10.20.177' # creates switchIP variable and defines its value, this is the mgmtIP address of the switch
interfaces = switchFunc(switchIP).json() # creates interfaces variable from switchFunc function .json
displayInterfaces = interfaces['imdata'] # creates displayInterfaces variable that assigns contents of "imdata" from interfaces

for interface in displayInterfaces: # for loop iterating through each interface in displayInterfaces
    print(interface['ipv4If']['attributes']['dn'] + '\t' + interface['ipv4If']['attributes']['id'])
    # print statement containing information for "dn" and "id" of each interface