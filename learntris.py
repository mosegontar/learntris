#!/usr/bin/env python

import sys

from grid import Grid
from tetraminos import *


class Operator(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()



    def display(self, active_tet=False):

        west  = self.active_tet.west
        east  = self.active_tet.east
        south = self.active_tet.south

        if not active_tet:


            if self.active_tet.shape:

                for index, row in enumerate(self.active_tet.shape):
                    
                    for num, cell in enumerate(row):

                        if cell:
                            self.active_tet.shape[index][num] = cell.lower()
                    
                    game.grid.board[index+south][west:east] = row

            else:
                pass

            game.grid.draw_board()

        else:

            game.grid.draw_board()

    def spawn_tet(self):
        
        west  = self.active_tet.west
        east  = self.active_tet.east
        south = self.active_tet.south

        for index, row in enumerate(self.active_tet.shape):

            for num, cell in enumerate(row):
                
                if cell:
                    self.active_tet.shape[index][num] = cell.upper()

            game.grid.board[index+south][west:east] = row

        self.display(True)


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
        
        if signal == '?s' or signal == '?n':
            signals = [signal]
        else:
            signals = [s for s in signal if s != ' ']

        for s in signals:

            commands = {'p' : game.display,
                        'q' : sys.exit, 
                        'g' : game.grid.given, 
                        'c' : game.grid.clear,
                        '?s': game.grid.show_score,
                        '?n': game.grid.show_clear_lines,
                        's' : game.grid.step,
                        't' : game.active_tet.print_tet,
                        ')' : game.active_tet.rotate_clockwise,
                        '(' : game.active_tet.rotate_counter_clockwise,
                        ';' : game.new_line,
                        'P' : game.spawn_tet,
                        '<' : game.active_tet.move_tet_west,
                        '>' : game.active_tet.move_tet_east,
                        'v' : game.active_tet.move_tet_south,
                        'V' : game.active_tet.hard_drop}

            if s.isupper() and not (s == 'V' or s == 'P'):
                self.active_tet = self.set_active_tet(s)
            else:
                commands[s]()


    def receive_signal(self):

        while True:

            received = raw_input()

            self.signal_parser(received)
            


if __name__ == '__main__':
    
    game = Operator()
    game.receive_signal()