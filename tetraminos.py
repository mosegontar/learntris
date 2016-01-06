#!/usr/bin/env python

class Tetramino(object):

    def __init__(self, shape=None):

        self.shape = shape

    def print_tet(self):

        if self.shape:
            for row in self.shape:
                row = map(lambda cell: '.' if cell == None else cell, row)
                print ' '.join(row)

        else:

            pass



class I_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, None, None, None],
                      ['c', 'c', 'c', 'c'],
                      [None, None, None, None],
                      [None, None, None, None]]

class O_tet(Tetramino):

    def __init__(self):

        self.shape = [['y', 'y'],
                      ['y', 'y']]

class Z_tet(Tetramino):

    def __init__(self):

        self.shape = [['r', 'r', None],
                      [None, 'r', 'r'],
                      [None, None, None]]