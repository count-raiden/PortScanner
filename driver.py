from main import scan_ports

targets = input("Enter targets to scan")
if "," in targets:
    for domain in targets.split(","):
        scan_ports(domain)
else:
    scan_ports(targets)