import json
import subprocess

f = open('devices.json')
 
devices = json.load(f)
f.close()


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

  print("Executing: ", " ".join(["ssh", ip, setup_command]))
  subprocess.call(["ssh", ip, setup_command], shell=True)

  print("Executing: ", " ".join(["ssh", ip, run_command]))
  subprocess.Popen(["ssh", ip, run_command], shell=True)