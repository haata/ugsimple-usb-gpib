# ugsimple-usb-gpib
Python3 libusb UGSimple GPIB Driver

Tested using Linux, should work for Mac OSX, Windows and any OS with Python libusb support.


## Setup

### Linux

It is recommended to add the udev rule so root isn't required.

```bash
sudo cp 98-ugsimple.rules /etc/udev/rules.d/.
sudo udevadm control --reload-rules
```


## Usage

Initialize UGSimpleGPIB

```python
from ugsimple.GPIB import UGSimpleGPIB
mygpib = UGSimpleGPIB()

```

Writing "my command" a command to address 0x02
```python
mygpib.write( 0x02, "my command" )
```

Reading from address 0x02
```python
data = mygpib.read( 0x02 )
print ( data )
```

Writting and reading the returned result using the ask() method
```python
device_id = mygpib.ask( 0x02, 'ID?' )
print ( device_id )
```

See ugsimple/GPIB.py for further documentation.


## Notes

Currently not well tested.
The USB command set for the UGSimple GPIB adapter should be complete but hasn't been tested with many devices yet.


Comments/Bug Reports/Patches welcome :D


