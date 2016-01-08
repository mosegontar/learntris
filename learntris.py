#!/usr/bin/env python

import sys

from grid import Grid
from tetraminos import *


class Operator(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()

    def spawn_tet(self):
        
        left = self.active_tet.spawn
        right =  left + self.active_tet.size

        for index, row in enumerate(self.active_tet.shape):
            
            for num, cell in enumerate(row):
                
                if cell:
                    row[num] = cell.upper()
                    self.active_tet.shape[index][num] = cell.upper()


            game.grid.board[index][left:right] = row

        game.grid.draw_board()


    def set_active_tet(self, block):

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

    def new_line(self):
        print

    def signal_parser(self, signal):
      
        signals = signal.split()

        for s in signals:

            commands = {'p' : game.grid.draw_board, 
                        'g' : game.grid.given, 
                        'c' : game.grid.clear,
                        '?s': game.grid.show_score,
                        '?n': game.grid.show_clear_lines,
                        's' : game.grid.step,
                        't' : game.active_tet.print_tet,
                        ')' : game.active_tet.rotate_clockwise,
                        ';' : self.new_line,
                        'P' : self.spawn_tet}

            if s == 'q':
                sys.exit()
            
            if s.isupper() and s != 'P':
                self.active_tet = self.set_active_tet(s)
            else:
                commands[s]()


    def receive_signal(self):

        while True:

            received =  raw_input()

            self.signal_parser(received)
            


if __name__ == '__main__':
    
    game = Operator()
    game.receive_signal()