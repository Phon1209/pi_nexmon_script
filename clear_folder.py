import json
import subprocess

f = open('devices.json')
 
devices = json.load(f)
f.close()

for device in devices:
  ip = f"{device['user']}@{device['ip']}"
  print(" ".join(["ssh", ip, "sudo rm -rf $(ls -d */)"]))

  subprocess.call(["ssh", ip, "sudo rm -rf $(ls -d */)"])