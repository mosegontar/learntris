#!/usr/bin/env python

from grid import Grid
from tetraminos import *

class Game(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()
        self.set_tets = False
        self.west  = None
        self.east  = None
        self.south = None

    def get_coordinates(self):

        self.west = self.active_tet.west
        self.east = self.active_tet.east
        self.south = self.active_tet.south

    def set_board(self, case_change):

        self.get_coordinates()

        if self.active_tet.shape:
        
            if self.west < 0:
                self.active_tet.west = 0
                self.active_tet.east = self.active_tet.west + len(self.active_tet.shape[0])
                self.get_coordinates()


            for index, row in enumerate(self.active_tet.shape):

                for num, cell in enumerate(row):
                    
                    if cell and case_change == 'lower':
                        self.active_tet.shape[index][num] = cell.lower()
                    elif cell:
                        self.active_tet.shape[index][num] = cell.upper()
                    else:
                        pass

                self.grid.board[index+self.south][self.west:self.east] = row


    def place_tets(self):

        self.set_board('lower')
        self.set_tets = True        

    def set_active_tet(self, block):

        if self.active_tet:
            self.place_tets()

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