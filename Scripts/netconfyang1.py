from collections import OrderedDict

interface = OrderedDict([ ("brand","Cisco"),("model","1941"),("mgmtIP","10.0.0.1"),("G0/0","10.0.1.1"),("G0/1","10.0.2.1"),("G0/2","10.1.0.1")])

for key,value in interface.items():
    print("Key = "+ key + "\t\t"+ "Value = "+ value)
