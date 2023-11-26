import json
from pathlib import Path
import subprocess

f = open('devices.json')

devices = json.load(f)
f.close()

destination_location = "C:\Users\Phon1209\Desktop\Work\CSI_data\channel_test"

files = [
    "ChulaWiFi_backroom_w100"
]

for device in devices:
    local_folder = f"./retrieved_data/{device['name']}"
    path = Path(local_folder)
    path.mkdir(parents=True, exist_ok=True)

    for file in files:
        remote_folder = f"{device['user']}@{device['ip']}:./{file}"
        print(" ".join(["scp", "-r", remote_folder, local_folder]))

        subprocess.Popen(["scp", "-r", remote_folder, local_folder])

