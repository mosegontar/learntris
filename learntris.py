#!/usr/bin/env python

import sys

from grid import Grid
from tetraminos import *


class Operator(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()


    def spawn_tet(self):
        
        west  = self.active_tet.west
        east  = self.active_tet.east
        south = self.active_tet.south

        for index, width in enumerate(self.active_tet.shape):
            
            for num, cell in enumerate(width):
                
                if cell:
                    width[num] = cell.upper()
                    self.active_tet.shape[index][num] = cell.upper()

            game.grid.board[index+south][west:east] = width

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

        if len(signals) == 1 and not (signals[0] == '?s' or signals[0] == '?n'):
            signals = signals[0]
        else:
            pass

        for s in signals:



            commands = {'p' : game.grid.draw_board,
                        'q' : sys.exit, 
                        'g' : game.grid.given, 
                        'c' : game.grid.clear,
                        '?s': game.grid.show_score,
                        '?n': game.grid.show_clear_lines,
                        's' : game.grid.step,
                        't' : game.active_tet.print_tet,
                        ')' : game.active_tet.rotate_clockwise,
                        '(' : game.active_tet.rotate_counter_clockwise,
                        ';' : self.new_line,
                        'P' : self.spawn_tet,
                        '<' : game.active_tet.move_tet_west,
                        '>' : game.active_tet.move_tet_east,
                        'v' : game.active_tet.move_tet_south}

            if s.isupper() and s != 'P':
                self.active_tet = self.set_active_tet(s)

            elif len(s) > 1 and not (s == '?s' or s == '?n'):
                for char in s:
                    s = char
                    commands[s]()
            else:
                commands[s]()


    def receive_signal(self):

        #while True:

            received =  "T ( >>>> > Pq" #raw_input()

            self.signal_parser(received)
            


if __name__ == '__main__':
    
    game = Operator()
    game.receive_signal()