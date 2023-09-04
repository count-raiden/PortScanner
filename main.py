import socket 
import threading 
from queue import Queue

print_lock = threading.Lock()

target = 'scanme.org'

def scan_ports(port):
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = socket_instance.connect((target,port))
        with print_lock:
            print("Port", port, "is open")

        connection.close()
    except:
        print("Port",port)

def threader():
    while True:
        worker = q.get()
        scan_ports(worker)
        q.task_done()

q = Queue()
for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True 
    t.start()

for worker in range(1,101):
    q.put(worker)

q.join()