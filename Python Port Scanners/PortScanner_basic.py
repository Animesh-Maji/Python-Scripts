import socket
from IPy import IP

def port_scan(ipaddr, port):
    try :
        sock = socket.socket()
        sock.settimeout(0.5) # this will try to connect to a port for the defined time either it will take long time to connect
        sock.connect((ipaddr,port))

        print("[+] The Port " + str(port) + " is open")

    except : 
        pass

        # print("[-] The port " + str(port) + " is closed")  I commented out this because we dont want to see all the closed ports

ipaddr = input("Enter the target Ip : ") 
portRange = input("Enter the port range (eg. 80-445) : ")

lowPort = int(portRange.split("-")[0])
highPort = int(portRange.split("-")[1])

for port in range(lowPort, highPort): 
    port_scan(ipaddr, port)