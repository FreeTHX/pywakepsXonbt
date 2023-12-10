# PyWakePlaystationX (ps3, ps4, ps5) On BlueTooth
This is a simple Python library to switch on a Sony ps3/ps4/ps5 using Bluetooth.  This version extends [the previous one developed for PlayStation 4 only](https://github.com/FreeTHX/pywakeps4onbt).

The main objective is to include it into [Home Assistant](https://www.home-assistant.io/ "Home Assistant") components to provide a "Wake PsX On Bt" service.

## How does it work ?
The Playstation with bluetooth controler can be simply switched on via :
- Spoofing a previously paired controler (SixAxis/DualShock3, DualShock4 or DualSense) BDADDR
- Initiating a HCI connection to the PlayStation BDADDR

## Supported Devices
The module tests the adapter support via a ```hci_read_local_manufacturer``` python implementation and read the ```manufacturer``` returned value from ```OCF_READ_LOCAL_VERSION```  
Currently supported adapters :
- Broadcom devices (```manufacturer = 15```)
- Cypress Semiconductor devices (```manufacturer = 305```)

## Get Bluetooth addresses over USB
Plug the DualShock3/4 or DualSense controler on your computer using micro USB cable.  
Once ```pywakepsXonbt``` is installed, run the following command from a python shell:
```python
>>> import wakepsXonbt
>>> wakepsXonbt.get_bt_addr()
{'type': 'dualshock3'/'dualshock4'/'dualsense', 'dsbt_address': '00:1F:E2:12:34:56', 'psXbt_address': '90:CD:B6:12:34:56'}
```

## No external dependency
Recent versions (0.7+) do not use external dependencies for bluetooth and HCI.