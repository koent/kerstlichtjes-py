# kerstlichtjes-py

Christmas lights API and web interface for ESP32 using MicroPython.

## Installation

1. Add current user to `dialout` group to enable interacting with ttyUSB0.
   1. `sudo usermod -aG dialout $USER`.
   1. Log out and back in.
1. Create a Python environment: `python -m venv .venv`.
1. Activate environment: `source .venv/bin/activate`.
1. Install required packages: `pip3 install esptool adafruit-ampy`.
1. Download and flash the latest MicroPython firmware. Follow [the instructions for ESP32](https://micropython.org/download/ESP32_GENERIC/).
1. Copy 'src/config-example.json' to 'src/config.json' and fill in.
1. Execute `deploy.sh`.
1. Restart the ESP32 (press the 'EN' button).

## Usage

Navigate to the ip address configured in 'src/config.json' using http. Clicking On/Off sets pin 5 high/low.

To view output over the serial port, run `screen /dev/ttyUSB0 115200`. Killing `screen` can be done by pressing `ctrl-a`, then `k`, then `y`.
