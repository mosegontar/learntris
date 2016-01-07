#!/usr/bin/env python

class Tetramino(object):

    def __init__(self, shape=None, size=None):

        self.shape = shape
        self.size = size

    def print_tet(self):

        if self.shape:
            for row in self.shape:
                row = [cell or '.' for cell in row]
                print ' '.join(row)
        else:
            pass

    def rotate_clockwise(self):

        self.shape = zip(*self.shape[::-1])


class I_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, None, None, None],
                      ['c',  'c',  'c',   'c'],
                      [None, None, None, None],
                      [None, None, None, None]]

        self.size = len(self.shape)



class O_tet(Tetramino):

    def __init__(self):

        self.shape = [['y', 'y'],
                      ['y', 'y']]

class Z_tet(Tetramino):

    def __init__(self):

        self.shape = [['r', 'r', None],
                      [None, 'r', 'r'],
                      [None, None, None]]

class S_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, 'g', 'g'],
                      ['g', 'g', None],
                      [None, None, None]]

class J_tet(Tetramino):

    def __init__(self):

        self.shape = [['b', None, None],
                      ['b', 'b', 'b'],
                      [None, None, None]]

class L_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, None, 'o'],
                      ['o', 'o', 'o'],
                      [None, None, None]]

class T_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, 'm', None],
                      ['m', 'm', 'm'],
                      [None, None, None]]

"""
i = I_tet()

first = i
first.print_tet()

i.shape = zip(*i.shape[::-1])
print
i.print_tet()
print

i.shape = zip(*i.shape[::-1])
i.print_tet()
print

i.shape = zip(*i.shape[::-1])
i.print_tet()

print

i.shape = zip(*i.shape[::-1])
i.print_tet()
print

z = Z_tet()
z.print_tet()
print

z.shape = zip(*z.shape[::-1])
z.print_tet()
print

z.shape = zip(*z.shape[::-1])
z.print_tet()
print

z.shape = zip(*z.shape[::-1])
z.print_tet()
print

z.shape = zip(*z.shape[::-1])
z.print_tet()
print
"""