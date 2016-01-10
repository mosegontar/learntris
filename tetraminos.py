#!/usr/bin/env python


class Tetramino(object):

    def __init__(self, shape=None, size=0, west=0, east=0, south=0):

        self.shape = shape
        self.size = size
        self.west = west
        self.east = east
        self.south = south 

    def print_tet(self):

        if self.shape:
            for row in self.shape:
                row = [cell or '.' for cell in row]
                print ' '.join(row)
        else:
            pass

    def rotate_clockwise(self):

        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def rotate_counter_clockwise(self):

        self.shape = [list(row) for row in zip(*self.shape)[::-1]]

    def set_coordinates(self):

        self.west = (10 - self.size) / 2
        self.east = self.west + self.size
        self.south = 0

        return (self.west, self.east, self.south)

    def move_tet_west(self):

        western_edges = [cell[0] for cell in self.shape]

        if self.west == 0 and any(western_edges):

            pass

        elif self.west == 0 and not any(western_edges):

            for index, row in enumerate(self.shape):
                self.shape[index].pop(0)
            

            self.west = self.west - 1
            self.east = self.east - 1            

        elif len(self.shape[0]) != self.size:

            for index, row in enumerate(self.shape):
                self.shape[index].append(None)

            self.west = self.west - 1
            self.east = self.east - 1


        else:
            self.west = self.west - 1
            self.east = self.east - 1


    def move_tet_east(self):

        eastern_edges = [cell[-1] for cell in self.shape]

        if self.east >= 10 and any(eastern_edges):

            pass
        
        elif self.east == 10 and not any(eastern_edges):

            for row in self.shape:
                row.pop(2)

            self.west = self.west + 1
            self.east = self.east + 1

        elif len(self.shape[0]) != self.size:

            for index, row in enumerate(self.shape):
                self.shape[index].insert(0, None)
            
            self.west = self.west + 1
            self.east = self.east + 1

        else:

            self.west = self.west + 1
            self.east = self.east + 1


    def move_tet_south(self):

        southern_bordern = self.shape[-1]

        if self.south + self.size > 22 and any(southern_bordern):
        
            pass

        elif self.south + self.size == 21 and not any(southern_bordern):

            self.shape.pop(-1)

            self.south = self.south + 1

        else:

            self.south = self.south + 1

    def hard_drop(self):

        distance_to_floor = 23 - (self.south + len(self.shape))

        for i in range(distance_to_floor):

            self.move_tet_south()


         
class I_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, None, None, None],
                      ['c',  'c',  'c',   'c'],
                      [None, None, None, None],
                      [None, None, None, None]]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west  = coordinates[0]
        self.east  = coordinates[1]
        self.south = coordinates[2]


class O_tet(Tetramino):

    def __init__(self):

        self.shape = [['y', 'y'],
                      ['y', 'y']]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]

class Z_tet(Tetramino):

    def __init__(self):

        self.shape = [['r', 'r', None],
                      [None, 'r', 'r'],
                      [None, None, None]]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]

class S_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, 'g', 'g'],
                      ['g', 'g', None],
                      [None, None, None]]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]


class J_tet(Tetramino):

    def __init__(self):

        self.shape = [['b',  None, None],
                      ['b',  'b',   'b'],
                      [None, None, None]]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]

class L_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, None,  'o'],
                      ['o',  'o',   'o'],
                      [None, None, None]]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]

class T_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, 'm', None],
                      ['m', 'm', 'm'],
                      [None, None, None]]

        self.size = len(self.shape)

        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]
