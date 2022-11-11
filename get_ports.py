import sys
import nmap

file = open("ports.txt", "a")
scanner = nmap.PortScanner()
hosts = []
active = []

host = "8.8.8.8"
result = scanner.scan(host, '1-1023', '-v')
if result['scan'][host]['status']['state'] != "down":
    for port in result['scan'][host].get("tcp", {}):
        if result['scan'][host]["tcp"][port]["state"] == "open":
            print(f"{host}:{port} is open.")
            active.append((host, port, result['scan'][host]["tcp"][port]))
    

file.write(f"Number of active ports: {len(active)}\n======================\n")
for a in active:
    file.write(str(a)+"\n")