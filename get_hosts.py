import sys
import nmap

file = open("hosts.txt", "a")
scanner = nmap.PortScanner()
hosts = []
active = []

for i in range(7):
    for j in range(255):
        host = f"89.43.{i}.{j}"
        result = scanner.scan(host, '1', '-v')
        if result['scan'][host]['status']['state'] != "down":
            print((host, result['scan'][host]['status']))
            active.append((host, result['scan'][host]['status']))
    

file.write(f"Number of active hosts: {len(active)}\n\n\n======================")
for a in active:
    file.write(a)