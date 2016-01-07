#!/usr/bin/env python

import sys

from grid import Grid
from tetraminos import *


class Operator(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()

    def set_active_set(self, block):

        i_tet = I_tet()
        o_tet = O_tet()
        z_tet = Z_tet()
        s_tet = S_tet()
        j_tet = J_tet()
        l_tet = L_tet()
        t_tet = T_tet()

        shapes = {'I': i_tet, 
                  'O': o_tet, 
                  'Z': z_tet, 
                  'S': s_tet,
                  'J': j_tet,
                  'L': l_tet,
                  'T': t_tet}

        return shapes[block]

    def signal_parser(self, signal):
      
        signals = signal.split()

        for s in signals:

            commands = {'p' : game.grid.draw_board, 
                        'g' : game.grid.given, 
                        'c' : game.grid.clear,
                        '?s': game.grid.show_score,
                        '?n': game.grid.show_clear_lines,
                        's' : game.grid.step,
                        't' : game.active_tet.print_tet}

            if s == 'q':
                sys.exit()
            
            if s.isupper():
                self.active_tet = self.set_active_set(s)
            else:
                commands[s]()


    def receive_signal(self):

        while True:

            received =  raw_input()

            self.signal_parser(received)
            


if __name__ == '__main__':
    
    game = Operator()
    game.receive_signal()