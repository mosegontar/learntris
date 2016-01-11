#!/usr/bin/env python

from grid import Grid
from tetraminos import *

class Game(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()
        self.west  = None
        self.east  = None
        self.south = None

    def check_for_collisions(self, direction):
        if direction == 'south':
            grid_status = []
            for row_num, row in enumerate(self.grid.board):
                for col, cell in enumerate(row):
                    if cell:
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


            """
            southern_most_row = self.active_tet.south + len(self.active_tet.shape) - 1
            southern_border = self.active_tet.shape[-1]

            live_row = self.grid.board[southern_most_row][self.active_tet.west:self.active_tet.east]
            
            if len(self.active_tet.shape) != self.active_tet.size:
                print southern_most_row, 'smr'
            if any(live_row):
                if not any(southern_border):
                    self.active_tet.shape.pop(-1)
                    self.active_tet.south = self.active_tet.south - 1
                else:
                    print 'hi' 
                    live_cells = [index for index, cell in enumerate(live_row) if cell]
                    for position in live_cells:
                        if southern_border[position]:
                            return True
                        print southern_most_row, self.active_tet.south

            """
        elif direction == 'west':

            southern_most_row = self.active_tet.south + len(self.active_tet.shape)
            western_edges = [cell[0] for cell in self.active_tet.shape]

            live_column = [cell[self.active_tet.west] for cell in self.grid.board[self.active_tet.south:southern_most_row]]
            if any(live_column):

                return True

    def move_tet_west(self):

        western_edges = [cell[0] for cell in self.active_tet.shape]

        if self.active_tet.west == 0 and any(western_edges):

            pass

        elif self.active_tet.west == 0 and not any(western_edges):

            for index, row in enumerate(self.active_tet.shape):
                self.active_tet.shape[index].pop(0)

            self.active_tet.west = self.active_tet.west - 1
            self.active_tet.east = self.active_tet.east - 1            

        elif len(self.active_tet.shape[0]) != self.active_tet.size:

            for index, row in enumerate(self.active_tet.shape):
                self.active_tet.shape[index].append(None)

            self.active_tet.west = self.active_tet.west - 1
            self.active_tet.east = self.active_tet.east - 1

            collision = self.check_for_collisions('west')
            if collision:
                
                for index, row in enumerate(self.active_tet.shape):
                    self.active_tet.shape[index].append(None)                
                self.active_tet.west = self.active_tet.west + 1
                self.active_tet.east = self.active_tet.east + 1
        else:
            self.active_tet.west = self.active_tet.west - 1
            self.active_tet.east = self.active_tet.east - 1
            
            collision = self.check_for_collisions('west')
            if collision:
                self.active_tet.west = self.active_tet.west + 1
                self.active_tet.east = self.active_tet.east + 1

    def move_tet_east(self):

        eastern_edges = [cell[-1] for cell in self.active_tet.shape]

        if self.active_tet.east >= 10 and any(eastern_edges):

            pass
        
        elif self.active_tet.east >= 10 and not any(eastern_edges):

            for index, row in enumerate(self.active_tet.shape):
                self.active_tet.shape[index].pop(2)

            self.active_tet.west = self.active_tet.west + 1
            self.active_tet.east = self.active_tet.east + 1

        elif len(self.active_tet.shape[0]) != self.active_tet.size:

            for index, row in enumerate(self.active_tet.shape):
                self.active_tet.shape[index].insert(0, None)
            
            self.active_tet.west = self.active_tet.west + 1
            self.active_tet.east = self.active_tet.east + 1

        else:
            self.active_tet.west = self.active_tet.west + 1
            self.active_tet.east = self.active_tet.east + 1


    def move_tet_south(self):

        southern_border = self.active_tet.shape[-1]

        if self.active_tet.south + len(self.active_tet.shape) > 21 and any(southern_border):
        
            pass

        elif self.active_tet.south + len(self.active_tet.shape) == 21 and not any(southern_border):

            self.active_tet.shape.pop(-1)
            self.active_tet.south = self.active_tet.south + 1
            
            collision = self.check_for_collisions('south')
            
            if collision:
                self.active_tet.south = self.active_tet.south - 1
                self.active_tet.shape.append([None]*self.active_tet.size)
        else:
            self.active_tet.south = self.active_tet.south + 1    
            collision = self.check_for_collisions('south')
            if collision:
                self.active_tet.south = self.active_tet.south - 1

    def hard_drop(self):

        #self.get_coordinates()

        distance_to_floor = 25 - self.active_tet.south - len(self.active_tet.shape)

        count = 0
        while count != distance_to_floor:
            count += 1
            self.move_tet_south()


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

                grid_row = self.grid.board[index+self.south][self.west:self.east]
                for i, c in enumerate(row):
                    if c:
                        grid_row[i] = c
                
                self.grid.board[index+self.south][self.west:self.east] = grid_row





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