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
        """Set the starting coordinates of the tetramino"""
        self.west = (10 - self.size) / 2
        self.east = self.west + self.size
        self.south = 0

        return (self.west, self.east, self.south)


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

        self.shape = [['r',  'r',  None],
                      [None, 'r',   'r'],
                      [None, None, None]]

        self.size = len(self.shape)
        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]

class S_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, 'g',   'g'],
                      ['g',  'g',  None],
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

        self.shape = [[None,  'm', None],
                      ['m',   'm',  'm'],
                      [None, None, None]]

        self.size = len(self.shape)
        coordinates = self.set_coordinates()
        self.west = coordinates[0]
        self.east = coordinates[1]
        self.south = coordinates[2]
