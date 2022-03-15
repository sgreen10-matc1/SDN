#!/usr/bin/env python3

import requests
import json
import urllib3
urllib3.disable_warnings() # This disables the unsecure request warning


"""
Modify these please
"""
switchuser='cisco'
switchpassword='cisco'

url='https://10.10.20.177/ins'
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
      "cmd": "hostname dist-swo1-9k",
      "version": 1
    },
    "id": 2
  }
]
response = requests.post(url,data=json.dumps(payload), verify=False, headers=myheaders,auth=(switchuser,switchpassword)).json()