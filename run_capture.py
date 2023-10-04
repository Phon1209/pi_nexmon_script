import json
from socket import timeout
import subprocess

f = open('devices.json')
 
devices = json.load(f)
f.close()

# MI: 64:64:4A:BB:40:20

folder = input("folder name: ")
description = input("description: ")
channel = input("WiFi channel: ")
width = input("WiFi Frequency: ")
mac = input("Mac Address: ")
time_slice = input("time per file(second): ")
file_count = input("file count: ")


setup_command = f"sudo bash ./setup.sh {channel} {width} {mac}"
run_command = f"sudo bash ./capture.sh {folder} '{description}' {time_slice} {file_count}"

for device in devices:
  ip = f"{device['user']}@{device['ip']}"

  subprocess.call(["ssh", ip, setup_command], shell=True)

for device in devices:
  ip = f"{device['user']}@{device['ip']}"

  subprocess.Popen(["ssh", ip, run_command], shell=True)
