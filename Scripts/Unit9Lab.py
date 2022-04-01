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

def vlanFunc(switchIP, vlanNum, vlanName): # creates vlanFunc with parameters of switchIP, vlanNum, and vlanName
    cookie = getCookie(switchIP) # defining cookie variable from getCookie function with parameter switchIP
    url = "https://"+switchIP+"/api/mo/sys.json" # defining url variable, concantenating switchIP

    payload = {
    "topSystem": {
        "children": [
        {
            "bdEntity": {
            "children": [
                {
                "l2BD": {
                    "attributes": {
                    "fabEncap": "vlan-" + vlanNum , # location of vlanNum, concantenated with vlan-
                    "name": vlanName # location of vlanName
                    }
                }
                }
            ]
            }
        }
        ]
    }
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + cookie # concatenating APIC-cookie with cookie value from getCookie function
}

    response = requests.request("POST", url, headers=headers, verify = False, data=json.dumps(payload)) # POST response, json.dumps with (payload)
    return response

def sviFunc(switchIP, sviInterface, ipAdd): # creates sviFunc with parameters of switchIP, sviInterface, and ipAdd
    cookie = getCookie(switchIP) # defining cookie variable from getCookie function with parameter switchIP
    url = "https://"+switchIP+"/api/mo/sys.json" # defining url variable, concantenating switchIP

    payload = {
    "topSystem": {
        "children": [
        {
            "ipv4Entity": {
            "children": [
                {
                "ipv4Inst": {
                    "children": [
                    {
                        "ipv4Dom": {
                        "attributes": {
                            "name": "default"
                        },
                        "children": [
                            {
                            "ipv4If": {
                                "attributes": {
                                "id": sviInterface # location one of sviInterface
                                },
                                "children": [
                                {
                                    "ipv4Addr": {
                                    "attributes": {
                                        "addr": ipAdd + "/24" # concatenating ipAdd with /24
                                    }
                                    }
                                }
                                ]
                            }
                            }
                        ]
                        }
                    }
                    ]
                }
                }
            ]
            }
        },
        {
            "interfaceEntity": {
            "children": [
                {
                "sviIf": {
                    "attributes": {
                    "adminSt": "up",
                    "id": sviInterface # location two of sviInterface
                    }
                }
                }
            ]
            }
        }
        ]
    }
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + cookie # concatenating APIC-cookie with cookie value from getCookie function
}

    response = requests.request("POST", url, headers=headers, verify = False, data=json.dumps(payload)) # POST response, json.dumps with (payload)
    return response

def hsrpFunc(switchIP, sviInterface, hsrpGrp, hsrpAdd): # creates hsrpFunc with parameters of switchIP, sviInterface, hsrpGrp, and hsrpAdd
    cookie = getCookie(switchIP) # defining cookie variable from getCookie function with parameter switchIP
    url = "https://"+switchIP+"/api/mo/sys.json" # defining url variable, concantenating switchIP

    payload = {
    "topSystem": {
        "children": [
        {
            "interfaceEntity": {
            "children": [
                {
                "sviIf": {
                    "attributes": {
                    "id": sviInterface # location one of sviInterface
                    }
                }
                }
            ]
            }
        },
        {
            "hsrpEntity": {
            "children": [
                {
                "hsrpInst": {
                    "children": [
                    {
                        "hsrpIf": {
                        "attributes": {
                            "id": sviInterface # location two of sviInterface
                        },
                        "children": [
                            {
                            "hsrpGroup": {
                                "attributes": {
                                "af": "ipv4",
                                "id": hsrpGrp, # location of hsrpGrp
                                "ip": hsrpAdd, # location of hsrpAdd
                                "ipObtainMode": "admin"
                                }
                            }
                            }
                        ]
                        }
                    }
                    ]
                }
                }
            ]
            }
        }
        ]
    }
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + cookie # concatenating APIC-cookie with cookie value from getCookie function
}

    response = requests.request("POST", url, headers=headers, verify = False, data=json.dumps(payload)) # POST response, json.dumps with (payload)
    return response

def ospfFunc(switchIP, sviInterface, ospfPro, ospfArea): # creates ospfFunc with parameters of switchIP, sviInterface, ospfPro, and ospfArea
    cookie = getCookie(switchIP) # defining cookie variable from getCookie function with parameter switchIP
    url = "https://"+switchIP+"/api/mo/sys.json" # defining url variable, concantenating switchIP

    payload = {
    "topSystem": {
        "children": [
        {
            "ospfEntity": {
            "children": [
                {
                "ospfInst": {
                    "attributes": {
                    "name": ospfPro # location of ospfPro
                    },
                    "children": [
                    {
                        "ospfDom": {
                        "attributes": {
                            "name": "default"
                        },
                        "children": [
                            {
                            "ospfIf": {
                                "attributes": {
                                "advertiseSecondaries": "yes",
                                "area": ospfArea, # location of ospfArea
                                "id": sviInterface # location one of sviInterface
                                }
                            }
                            }
                        ]
                        }
                    }
                    ]
                }
                }
            ]
            }
        },
        {
            "interfaceEntity": {
            "children": [
                {
                "sviIf": {
                    "attributes": {
                    "id": sviInterface # location two of sviInterface
                    }
                }
                }
            ]
            }
        }
        ]
    }
    }
    
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'APIC-cookie=' + cookie # concatenating APIC-cookie with cookie value from getCookie function
}

    response = requests.request("POST", url, headers=headers, verify = False, data=json.dumps(payload)) # POST response, json.dumps with (payload)
    return response

def addNewIP(ipAdd, octet, octetPosition): # creates addNewIP function with interface IP address, octet, and octet position parameters defined
  octetAdjNumb = octet - 1 # adjusts for python numbering system and corrects it by subtracting 1 from octet, step 1 (ex. 1,2,3 translates to 0,1,2)
  octets = ipAdd.split(".") # creates octets variable from ipAdd.split with period "." character as the identified delimiter value, this totals to "4" octets, step 2
  octetCombPosition = int(octets[octetAdjNumb]) + octetPosition # combines first 2 steps by associating the fixed position and how many octets were created, step 3
  octetStrType = str(octetCombPosition) # creates octetStrType variable by converting octetCombPosition to a string data type, step 4
  octets[octetAdjNumb] = octetStrType # combines step 1 and 2 to step 3, puts together (octets spacing created) with (adjusted fixed position) to (octetStrType string)
  newIpAdd = octets[0] + "." + octets[1] + "." + octets[2] + "." + octets[3] # defines newIpAdd variable, created from, octets + "."" character as delimiter
  return newIpAdd # returns newIpAdd to be called later for main script portion

# Main

devices = { # creates devices dictionary
    'dist-sw01' : {
        'hostname' : 'dist-sw01',
        'deviceType' : 'switch',
        'mgmtIP' : '10.10.20.177'
    },
    
    'dist-sw02' : {
        'hostname' : 'dist-sw02',
        'deviceType' : 'switch',
        'mgmtIP' : '10.10.20.178'
        }
    }

vlanNum = '110' # defining the value of vlanNum, vlan110
vlanName = 'testNXOS' # defining the value of vlanName, testNXOS
sviInterface = 'vlan110' # defining the value of sviInterface, vlan110
ipAdd = '172.16.110.1' # defining the value of ipAdd, ip address starting at 172.16.110.1, will use this for the for loop to increase by 1 for each switch
hsrpGrp = '10' # defining the value of hsrpGrp, hsrp 10
hsrpAdd = '172.16.110.1' # defining the value of hsrpAdd, ip address 172.16.110.1
ospfPro = '1' # defining the value of ospfPro, ospf process 1
ospfArea = '0.0.0.0' # defining the value of ospfArea, ospf area 0.0.0.0

for device in devices.values(): # for loop iterating through devices.values
    switchIP = device['mgmtIP'] # defining switchIP to whatever the value is for objects labeled "mgmtIP"

    newVlan = vlanFunc(switchIP, vlanNum, vlanName)
    # newVlan created from vlanFunc with all parameters now defined
    ipAdd = addNewIP(ipAdd, 4, 1)
    # ipAdd created from addNewIP with all parameters now defined, This incrementally adds "1" to the 4th octet
    newSVI = sviFunc(switchIP, sviInterface, ipAdd)
    # newSVI created from sviFunc with all parameters now defined
    newHSRP = hsrpFunc(switchIP, sviInterface, hsrpGrp, hsrpAdd)
    # newHSRP created from hsrpFunc with all parameters now defined
    newOSPF = ospfFunc(switchIP, sviInterface, ospfPro, ospfArea)
    # newOSPF created from ospfFunc with all parameters now defined