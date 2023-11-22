import json
from multiprocessing.connection import wait
from socket import timeout
import subprocess
from time import sleep

f = open('devices.json')

devices = json.load(f)
f.close()


folder = input("folder name: ")
description = input("description: ")
beacon = input("Only beacon frame(Y/n): ")
time_slice = input("Capture time: ")

beaconBool = (beacon.capitalize() == "Y")
run_command = f"sudo bash ./capture.sh {folder} '{description}' {time_slice} 1"

for device in devices:
    print(f"device: {device['user']}")
    print(
        f"Reading at channel {device['channel']}/{device['frequency']} on '{device['mac_address']}'")

input("Confirm the information above?")

for device in devices:
    ip = f"{device['user']}@{device['ip']}"

    setup_command = f"sudo bash ./setup.sh {device['channel']} {device['width']} {device['mac_address']}"
    subprocess.Popen(["ssh", ip, setup_command], shell=True)

sleep(5)
for device in devices:
    ip = f"{device['user']}@{device['ip']}"

    subprocess.Popen(["ssh", ip, run_command], shell=True)
