import socket 
import time 
from IPy import IP
from IPython.display import clear_output

def get_banner(sock):
    return sock.recv(1024)

def loading_screen(port):
    print("Port "+str(port)+" is closed", end='',flush=True)
    time.sleep(0.5)
    clear_output(wait=True)

def resolve_ip(ip_address):
    try:
        IP(ip_address)
        return ip_address
    except ValueError:
        return socket.gethostbyname(ip_address)

def scan_ports(domain):
    ip_address = resolve_ip(domain)
    print("Target resolves to the IP address:",ip_address)
    for port in range(1,101):
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.settimeout(0.5)
        try:
            socket_instance.connect((ip_address,port))
            try:
                banner = get_banner(socket_instance)
                print("[+] Open Port " + str(port) + " : " + str(banner.decode().strip('\n')))
            except:
                print("[+] Open Port " + str(port) +": No further information available")
        except:
            loading_screen(port)
        socket_instance.close()                