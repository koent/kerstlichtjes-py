import network
import json

print()
print("Starting Kerstlichtjes 2025")

with open('config.json', 'r') as f:
    config = json.load(f)

print("Connecting to WLAN...")

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ifconfig = tuple(config['network'][setting] for setting in ['ip', 'mask', 'gateway', 'dns'])
wlan.ifconfig(ifconfig)

wlan.connect(config['connection']['ssid'], config['connection']['password'])

print("Connected")
