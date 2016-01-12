#!/usr/bin/env python
import sys
from grid import Grid
from tetraminos import *

class Game(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()

    def check_for_collisions(self):
        """Checks for any collisions between active_tet and cemented cells on grid"""
        grid_status = []
        for row_num, row in enumerate(self.grid.board):
            for col, cell in enumerate(row):
                if cell and cell.islower():
                    grid_status.append((row_num, col))

        tet_status = []
        for row_num, row in enumerate(self.active_tet.shape):
            for col, cell in enumerate(row):
                if cell:
                    r = row_num + self.active_tet.south
                    c = col + self.active_tet.west
                    tet_status.append((r, c))

        if set(grid_status).intersection(set(tet_status)):
            return True

    def move_tet_west(self):
        """Attempts to move tetramino one degree westwardd"""

        western_edges = [cell[0] for cell in self.active_tet.shape]

        if self.active_tet.west <= 0 and any(western_edges):

            pass

        elif self.active_tet.west == 0 and not any(western_edges):

            self.active_tet.west -= 1
            self.active_tet.east -= 1

            collision = self.check_for_collisions()
            if collision:
                self.move_tet_east()
                return

            for index, row in enumerate(self.active_tet.shape):
                self.active_tet.shape[index].pop(0)

        else:

            if len(self.active_tet.shape[0]) != self.active_tet.size:
                for index, row in enumerate(self.active_tet.shape):
                    self.active_tet.shape[index].append(None)

            self.active_tet.west -= 1
            self.active_tet.east -= 1

            collision = self.check_for_collisions()
            if collision:
                self.move_tet_east()


    def move_tet_east(self):
        """Attempts to move tetramino one degree eastward"""

        eastern_edges = [cell[-1] for cell in self.active_tet.shape]

        if self.active_tet.east >= 10 and any(eastern_edges):

            pass

        elif self.active_tet.east > 10 and not any(eastern_edges):

            self.active_tet.west += 1
            self.active_tet.east += 1

            collision = self.check_for_collisions()
            if collision:
                self.move_tet_east()
                return

            # Shave off the empty, eastern-most row
            for index, row in enumerate(self.active_tet.shape):
                self.active_tet.shape[index].pop(2)

        else:

            if len(self.active_tet.shape[0]) != self.active_tet.size:

                for index, row in enumerate(self.active_tet.shape):
                    self.active_tet.shape[index].insert(0, None)

            self.active_tet.west += 1
            self.active_tet.east += 1


            collision = self.check_for_collisions()

            if collision:
                self.move_tet_west()


    def move_tet_south(self):
        """Attempts to move tetramino one degree southward"""

        southern_border = self.active_tet.shape[-1]

        if self.active_tet.south + len(self.active_tet.shape) > 21 and any(southern_border):

            pass

        elif self.active_tet.south + len(self.active_tet.shape) == 21 and not any(southern_border):

            self.active_tet.shape.pop(-1)
            self.active_tet.south += 1
            
            collision = self.check_for_collisions()
            
            if collision:
                self.active_tet.south -= 1
                self.active_tet.shape.append([None]*self.active_tet.size)
        else:
            self.active_tet.south += 1
            collision = self.check_for_collisions()
            if collision:
                self.active_tet.south -= 1


    def hard_drop(self):
        """Drops tetramino as far south as possible, until floor hit or collision"""

        distance_to_floor = 25 - self.active_tet.south - len(self.active_tet.shape)

        count = 0
        while count != distance_to_floor:
            count += 1
            self.move_tet_south()


    def set_board(self, case_change):
        """Updates the state of the game's grid"""

        # passed over if the grid has no Tetraminos on it.
        if self.active_tet.shape:
            
            # western coordinate is reset to zero if it dropped below zero;
            # this prevents blocks from showing up in the wrong palce.
            # If the western coordinate is less than zero, it means that the block is at the west wall
            if self.active_tet.west < 0:
                self.active_tet.west = 0
                self.active_tet.east = self.active_tet.west + len(self.active_tet.shape[0])

            for index, row in enumerate(self.active_tet.shape):

                for num, cell in enumerate(row):
                    
                    if cell and case_change == 'lower':
                        self.active_tet.shape[index][num] = cell.lower()
                    elif cell:
                        self.active_tet.shape[index][num] = cell.upper()
                    else:
                        pass

                # grid_row = elements currently on grid at the current position in question     
                # We find the appropriate row on the board to update by adding the index of the active_tet's current row 
                # to it's southern coordinate. For example, southern coordinates begin at 0, so the first row of a
                # tet that hasn't dropped yet is index=0 + self.active_tet.south=0, and we can therefore determine which
                # row on the game grid is being updated.  
                grid_row = self.grid.board[index+self.active_tet.south][self.active_tet.west:self.active_tet.east]
                
                # integrates the cells in the tetramino's row into the grid_row
                for i, c in enumerate(row):
                    if c:
                        grid_row[i] = c
                    else:
                        pass

                # cements the updated grid_row array to the appropriate section on the board
                self.grid.board[index+self.active_tet.south][self.active_tet.west:self.active_tet.east] = grid_row
        
        else:
            pass

    def place_tets(self):

        self.set_board('lower')

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