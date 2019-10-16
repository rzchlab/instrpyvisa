# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:30:57 2019

@author: rzchlab
"""

from time import sleep
from math import sqrt

class MotionControllerNewportESP300(object):
    def __init__(self, address, resource_manager, verbose=False):
        idstr = f'GPIB::{address}::INSTR'
        self.instr = resource_manager.get_instrument(idstr)
        self.verbose = verbose

    def write(self, cmd):
        self.instr.write(cmd)
        if self.verbose:
            print(cmd)

    def motoron(self, axis):
        """Turn motor on, axis is int."""
        self.write(f'{axis:d}MO')
        
    def move(self, axis, mm, block=True, wait_safety_factor=2):
        """Move relative in millimeters"""
        self.write(f'{axis:d}PR{mm:.5f}')
        if block:
            # Default values. Should be read instead.
            v = 0.2 #mm/s
            a = 0.8 #mm/s2
            # Accel time
            t_a = v/a # s
            # Accel distance
            d_a = 0.5 * v * t_a # mm
            # Distance less than acceleration distance
            if abs(mm) < d_a:
                t_tot = sqrt(0.5 * abs(mm) / a)
            # Distance greater than acceleration distance (max velocity reached)
            else:
                t_tot = (mm - d_a)/v + t_a
            sleep(wait_safety_factor * abs(t_tot))
        
    def move_um(self, axis, um, block=True, wait_safety_factor=2):
        return self.move(axis, um / 1000, block, wait_safety_factor)

if __name__ == '__main__':
    import visa as vs
    rm = vs.ResourceManager()
    mc = MotionControllerNewportESP300(20, rm, verbose=True)