# Python Interface for Sartorius Scales.

2010-2011 Robert Gieseke - robert.gieseke@gmail.com

MIT license, see LICENSE.

### Example usage:
    from sartorius import Sartorius
    scale = Sartorius('COM1')

    print scale.value()
    # zero scale
    scale.zero()
    print scale.value()

### Requirements:
pySerial - <http://pyserial.sourceforge.net/>

### Manual:
Sartorius - Description of the Interface
for EA, EB, GD, GE and TE Balances/Scales

