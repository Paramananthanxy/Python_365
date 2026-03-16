import ipaddress

ip = ipaddress.ip_address("192.168.33.1")
network = ipaddress.ip_network("192.168.33.0/24")

print(ip in network)