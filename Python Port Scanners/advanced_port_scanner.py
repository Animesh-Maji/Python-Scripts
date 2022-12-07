from argparse import ArgumentParser
import socket,time
from IPy import IP

''' Code Starts from here '''

def input_args():
    parser=ArgumentParser(description="** This is a command line based port scanner that is written in python. This does a very basic enumeration of ports and there banners if possible. Hope you like it. **", usage="Minimal usage : %(prog)s <ip addr>", epilog="Usage : %(prog)s -s <starting_port> -e <ending_port> <ip_addr>")
    parser.add_argument(metavar="IPv4 (Ip address)",dest="ip",help="Target IP")
    parser.add_argument("-s","--start",dest="sport",metavar="",type=int,default=1,help="Specify the starting port")
    parser.add_argument("-e","--end",dest="eport",metavar="",type=int,default=1024,help="Specify the ending port")
    parser.add_argument("--version",action="version",version="%(prog)s v1.1",help="To display the version")

    return parser.parse_args()

def domain_converter(ipaddr):
    try:
        IP(ipaddr)
        return ipaddr
    except ValueError :
        domain_to_IP = socket.gethostbyname(ipaddr)
        return domain_to_IP

def ip_resolver(ipaddr,sport,eport):
    t = time.localtime()
    scan_start_time = time.strftime("%H:%M:%S", t)
    converted_ip = domain_converter(ipaddr)
    print(f"\nStarting scan at : {scan_start_time}")
    print(f"---------------Scanning for {ipaddr} ---------------\n")
    for port in range(sport, eport+1):
        port_scanner(converted_ip,port)

def port_scanner(ipaddr,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        s.connect((ipaddr,port))
        try:
            banner = s.recv(1024).decode()
            print(f"[+] Port {port} is open ------- service : {banner}")
        except:
            print(f"[+] Port {port} is open")
    except:
        pass

if __name__ == '__main__':
    arguments=input_args()
    ip_resolver(arguments.ip,arguments.sport,arguments.eport)
