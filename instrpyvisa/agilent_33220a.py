# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 15:38:39 2019

@author: rzchlab
"""

class FuncGenAgilent33220(object):
    def __init__(self, address, resource_manager, verbose=False):
        idstr = f'GPIB::{address}::INSTR'
        self.instr = resource_manager.get_instrument(idstr)
        self.verbose = verbose
        
    def outp(self, state):
        """Turn output on (state=1) or off (state=0)."""
        state_str = 'OFF' if state == 0 else 'ON'
        self.write(f'OUTP {state_str};')
        
    def outp_on(self):
        """Turn output on (state=1) or off (state=0)."""
        self.outp(1)
        
    def outp_off(self):
        """Turn output on (state=1) or off (state=0)."""
        self.outp(0)
        
    def setup_sin(self, freq, vpp, offset):
        """
        Setup a sin wave output
        
        Args:
            freq: frequency in hz
            vpp: peak to peak voltage
            offset: offset in volts
        """
        cmd = (f"FUNC SIN; FREQ {freq:.3f}; VOLT {vpp:.3f};"
                f" VOLT:OFFS {offset:.3f};")
        print(cmd)
        self.instr.write(cmd)
        
    def offset(self, v_offset):
        """Change offset votage"""
        cmd = f" VOLT:OFFS {v_offset:.3f};"
        self.write(cmd)
        
    def write(self, cmd):
        self.instr.write(cmd)
        if self.verbose:
            print(cmd)
        
if __name__ == '__main__':
    import visa as vs
    rm = vs.ResourceManager()
    fg = FuncGenAgilent33220(10, rm, verbose=True)