#!/usr/bin/env python

from grid import Grid
from tetraminos import *

class Game(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()

    def spawn_tet(self):
        
        west  = self.active_tet.west
        east  = self.active_tet.east
        south = self.active_tet.south

        for index, row in enumerate(self.active_tet.shape):

            for num, cell in enumerate(row):
                
                if cell:
                    self.active_tet.shape[index][num] = cell.upper()

            self.grid.board[index+south][west:east] = row

    def update(self, active_tet=False):

        west  = self.active_tet.west
        east  = self.active_tet.east

        if self.active_tet.shape:
            if len(self.active_tet.shape) != self.active_tet.size:
                south = self.active_tet.south
            else:
                south = self.active_tet.south - 1

        if self.active_tet.shape:

            for index, row in enumerate(self.active_tet.shape):
                
                for num, cell in enumerate(row):

                    if cell:
                        self.active_tet.shape[index][num] = cell.lower()
                
                self.grid.board[index+south][west:east] = row

        else:
            pass

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