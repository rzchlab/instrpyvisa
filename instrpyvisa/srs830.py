# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:32:30 2019

@author: rzchlab
"""

class LockInAmpSrs830(object):
    def __init__(self, address, resource_manager, verbose=False):
        idstr = f'GPIB::{address}::INSTR'
        self.instr = resource_manager.get_instrument(idstr)
        self.verbose = verbose
        
    def rtheta(self):
        self.write('SNAP? 3,4')
        return self.instr.read_ascii_values()
    
    def write(self, cmd):
        self.instr.write(cmd)
        if self.verbose:
            print(cmd)
            
if __name__ == '__main__':
    import visa as vs
    rm = vs.ResourceManager()
    lia = LockInAmpSrs830(9, rm, verbose=True)