import json
f = open('devices.json')
devices = json.load(f)

devs = []
for dev in devices:
    devs.append(dev['ip'])

# devs.sort()
print(f"len: {len(devs)}")
for dev in devs:
    print(dev)
