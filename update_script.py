import json
import subprocess

f = open('devices.json')
 
devices = json.load(f)
f.close()

for device in devices:
  print(" ".join(["scp", "setup.sh", "capture.sh", f"{device['user']}@{device['ip']}:./"]))

  subprocess.call(["scp", "setup.sh", "capture.sh", f"{device['user']}@{device['ip']}:./"])