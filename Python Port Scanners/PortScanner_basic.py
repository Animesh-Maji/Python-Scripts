import socket
from IPy import IP

def port_scan(ipaddr, port):
    try :
        sock = socket.socket()
        sock.settimeout(0.5) # this will try to connect to a port for defined time either this take long time to connect
        sock.connect((ipaddr,port))
        print("[+] The Port " + str(port) + " is open")
    except : 
        pass
        # print("[-] The port " + str(port) + " is closed")

ipaddr = input("Enter the target Ip : ")

for port in range(130,140):
    port_scan(ipaddr, port)