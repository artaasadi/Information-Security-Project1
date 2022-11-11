import sys
import nmap
import socket

file = open("hosts.txt", "a")
scanner = nmap.PortScanner()
for i in range(7):
    for j in range(255):
        host = f"89.43.{i}.{j}"
        result = scanner.scan(host, '1', '-v')
        if result['scan'][host]['status']['state'] != "down":
            print(result)