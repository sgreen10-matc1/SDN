import json
import requests

net_controller = {"name": "localhost:58000",
                  "username": "student",   # Change the username to match the username set up in lab
                  "password": "cisco"  #Change password to match password set up in lab
                  }


def get_ticket(controller,username,password):
    api_url = "http://{}/api/v1/ticket".format(controller)

    headers = {
        "content-type": "application/json"
        }

    body_json = {
        "username": username,
        "password": password
        }

    response = requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)

    # print("Ticket request status: ",response.status_code)

    response_json = response.json()

    ticket = response_json["response"]["serviceTicket"]
    #print("The service ticket number is: ", ticket)

    return ticket

def get_hosts(cont,auth_ticket):
    host_url="http://{}/api/v1/host".format(cont)
    headers = {"X-Auth-Token": auth_ticket}
    response = requests.get(host_url,headers=headers,verify=False)

    #print("Request status: ",response.status_code)

    hosts=response.json()["response"]
    return hosts

def get_devices(cont, auth_ticket):
    host_url="http://{}/api/v1/network-device".format(cont)
    headers = {"X-Auth-Token":auth_ticket}
    response = requests.get(host_url,headers=headers,verify=False)

    #print("Request status: ",response.status_code)

    devices=response.json()["response"]
    return devices



def get_single_device(cont,auth_ticket,dev_id):
    host_url="http://{}/api/v1/network-device/{}".format(cont,dev_id)
    headers = {"X-Auth-Token":auth_ticket}
    response = requests.get(host_url,headers=headers,verify=False)
    return response.json()
def run_flow_analysis(cont,auth_ticket,source_ip, destination_ip):
    base_url = "http://{}/api/v1/flow-analysis".format(cont)
    headers = {"X-Auth-Token":auth_ticket}

    # initiate flow analysis
    body = {"destIP": destination_ip, "sourceIP": source_ip}
    initiate_response = requests.post(base_url, headers=headers, verify=False,
                                      json=body)
    flowAnalysisId = initiate_response.json()["response"]["flowAnalysisId"]
    detail_url = base_url + "/{}".format(flowAnalysisId)
    detail_response = requests.get(detail_url, headers=headers, verify=False)
    while not detail_response.json()["response"]["request"]["status"] == "COMPLETED":  # noqa: E501
        print("Flow analysis not complete yet, waiting 5 seconds")
        #sleep(5)
        detail_response = requests.get(detail_url, headers=headers,
                                       verify=False)

    # Return the flow analysis details
    return detail_response.json()["response"]

'''
def print_flow_analysis(flow, devices, source_ip, destination_ip, serviceTicket):
    
    # get a list of hosts and devices to devices to print out detail
    
    hosts = get_hosts(controller, serviceTicket)
    devices = get_devices(controller, serviceTicket)
    
    # beginng printing
    
    print("Name\t\tType\t\t\tPlateform\t\tStatus\t\tMnged IP\t\tUPtime")
    
    for flowDevice in flow['networkElementsInfo'] :
        print (flowDevice['name'], end='')
        print ("\t\t", end ='')
        if flowDevice["Id"] in str(hosts) :
            print ("PC"+ "\t" *8, end='')
            print(flowDevice["ip"]+"\t\t", end='')
        else:
            device = get_single_device(controller, serviceTicket, flowDevice['id'])
'''

'''def priHosDev(devices): # creates printDevInt function with intList as the parameter
    for host in devices: # for loop iterating through all interfaces in intList
            host_Name = host["response"][0]["hostName"] # creates ipAddInt variable, from intList, with the IP addresses of each interface
            host_IP = host["response"][0]["hostIp"] # creates maskInt variable, from intList, with the subnet mask of each interface
            print(host_Name + "\t\t" + host_IP) # prints each interface name, the IP address, and the subnet mask
     '''
     
     
######MAIN

#define intial variables for main
controller = net_controller["name"] #URL from Dictionary defined above
username = net_controller["username"]  #Username from Dictionary defined above
password = net_controller["password"]   #Password from Dictionary defined above

serviceTicket = get_ticket(controller,username,password)
devices=get_devices(controller,serviceTicket)
#printHost = priHosDev(devices)

#host_Name = net_controller["hostName"] # creates ipAddInt variable, from intList, with the IP addresses of each interface
#host_IP = net_controller["response"]["hostIp"]
print('')
#serviceTicket = get_ticket(controller,username,password)
#print(serviceTicket)

hosts=get_hosts(controller,serviceTicket)
print('')
print(hosts)

#print(net_controller)

connectIntFaceName = hosts['connectedInterfaceName']
print('')


for interface in hosts:
    hostMAC = interface['hostMac']
    host_NAME = interface['hostName'][0]
    #for h in [hosts][0]:
        #print(h)
    hostTPE = interface['hostType']
    ID = interface['id']
print(host_NAME+"\t"+ID+"\t"+hostTPE+"\t")


print('')
print('')

for host in hosts:
    hostMAC = host['hostMac']
    host_NAME = host['hostName'][0]
    for h in [hosts][0]:
        print(h)
        hostTPE = host['hostType']
        ID = host['id']
print(host_NAME+"\t"+ID+"\t"+hostTPE+"\t")

print(connectIntFaceName)


print('')
# priHosDev(devices)

#print('')
#devices=get_devices(controller,serviceTicket)
#print(devices)

#device= get_single_device(cont,serviceTicket,dev_id)
#print(device)

#print('')
#flow = run_flow_analysis(controller,serviceTicket,source_ip, destination_ip)
#print(flow)


# "Name" + host_NAME + "\n"+"Type" + hostTPE + "\n"+"id" + ID + "\n"