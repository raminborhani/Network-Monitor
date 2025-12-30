from ping3 import ping
import csv
from datetime import datetime

ips = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.1.1"
]

results = []

for ip in ips:
    response = ping(ip, timeout=2)
    status = "UP" if response else "DOWN"

    results.append({
        "IP": ip,
        "Status": status,
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

with open("network_report.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["IP", "Status", "Time"])
    writer.writeheader()
    writer.writerows(results)

print("Network monitoring completed. Report saved.")
