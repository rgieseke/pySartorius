# -*- coding: utf-8 -*-

"""
Python Interface for
Sartorius Serial Interface for
EA, EB, GD, GE, TE scales.

2010-2011 Robert Gieseke - robert.gieseke@gmail.com
See LICENSE.
"""

import serial

class Sartorius(serial.Serial):
    def __init__(self, com_port):
        """
        Initialise Sartorius device.

            Example:
            scale = Sartorius('COM1')
        """
        serial.Serial.__init__(self, com_port)
        self.baudrate = 9600
        self.bytesize = 7
        self.parity = serial.PARITY_ODD
        self.timeout = 0.5

    def value(self):
        """
        Return displayed scale value.
        """
        try:
            if self.inWaiting() == 0:
                self.write('\033P\n')
            answer = self.readline()
            if len(answer) == 16: # menu code 7.1.1
                answer = float(answer[0:11].replace(' ', ''))
            else: # menu code 7.1.2
                answer = float(answer[6:17].replace(' ',''))
            return answer
        except:
            return "NA"

    def display_unit(self):
        """
        Return unit.
        """
        self.write('\033P\n')
        answer = self.readline()
        try:
            answer = answer[11].strip()
        except:
            answer = ""
        return answer

    def tara_zero(self):
        """
        Tara and zeroing combined.
        """
        self.write('\033T\n')

    def tara(self):
        """
        Tara.
        """
        self.write('\033U\n')

    def zero(self):
        """
        Zero.
        """
        self.write('\033V\n')
