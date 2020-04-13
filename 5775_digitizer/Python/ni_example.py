# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:30:39 2020

@author: strobe
"""

from nifpga import Session


with Session("C:/Users/strobe/Desktop/example_digitizer_vi/FPGA Bitfiles/PXIe_5775_KU040.lvbitx", "RIO0") as session:
    my_control = session.registers['My Control']
    my_indicator = session.registers['My Indicator']
    my_control.write(4)
    data = my_indicator.read()
    print(data)  # prints 16