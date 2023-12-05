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
time_slice = input("Capture time: ")

run_command = f"sudo bash ./capture.sh {folder} '{description}' {time_slice} 1"
print()
for device in devices:
    print(f"device: {device['name']}: {device['ip']}")
    print(
        f"Reading at channel {device['channel']}/{device['frequency']} on '{device['mac_address']}'")
    if device['filter'] != "":
        print(
            f"Filter on {device['filter']} frame"
        )
    print()

input("Confirm the information above?")

setup_processes = []
for device in devices:
    ip = f"{device['user']}@{device['ip']}"

    if device['filter'] != "":
        setup_command = f"sudo bash ./setup.sh {device['channel']} {device['frequency']} {device['mac_address']} {device['filter']}"
    else:
        setup_command = f"sudo bash ./setup.sh {device['channel']} {device['frequency']} {device['mac_address']}"

    setup_processes.append(subprocess.Popen(
        ["ssh", ip, setup_command]))

# Wait for all setup subprocesses to finish
for setup_process in setup_processes:
    setup_process.wait()

input("Press any key to start the command...")
for device in devices:
    ip = f"{device['user']}@{device['ip']}"

    subprocess.Popen(["ssh", ip, run_command], shell=True)
