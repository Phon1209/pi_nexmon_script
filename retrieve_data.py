import json
import subprocess

f = open('devices.json')
 
devices = json.load(f)
f.close()

files = [
  "ISEL_R36_T36_1000"
]

for device in devices:
  local_folder = f"./retrieved_data/{device['name']}"

  for file in files:
    remote_folder = f"{device['user']}@{device['ip']}:./{file}"
    print(" ".join(["scp", "-r", remote_folder, local_folder]))

    subprocess.call(["scp", "-r", remote_folder, local_folder])