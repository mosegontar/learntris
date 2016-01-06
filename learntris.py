#!/usr/bin/env python

import sys

class Grid(object):

    def __init__(self):
        self.board = [[None] * 10 for i in range(22)]
        self.score = 0
        self.lines_clear = 0

    def draw_board(self):

        current_board = self.board
        
        for row in current_board:
            row = map(lambda cell: '.' if cell == None else cell, row)
            print ' '.join(row)

    def given(self):
        
        for index, row in enumerate(self.board):
            self.board[index] = [None if cell == '.' else cell 
                                 for cell in raw_input() if cell != ' ']

    def clear(self):
        self.board = [[None] * 10 for i in range(22)]

    def show_score(self):
        print self.score

    def show_clear_lines(self):
        print self.lines_clear

    def step(self):
        for index, row in enumerate(self.board):
            if all(row) and row[0] != None:
                self.board[index] = [None] * 10
                self.score += 100
                self.lines_clear += 1



class Tetramino(object):

    def __init__(self, shape=None):

        self.shape = shape

    def print_tet(self):

        for row in self.shape:
            row = map(lambda cell: '.' if cell == None else cell, row)
            print ' '.join(row)



class I_tet(Tetramino):

    def __init__(self):

        self.shape = [[None, None, None, None],
                      ['c', 'c', 'c', 'c'],
                      [None, None, None, None],
                      [None, None, None, None]]



class Operator(object):

    def __init__(self):

        self.grid = Grid()
        self.active_tet = Tetramino()

    def set_active_set(self, block):

        i_tet = I_tet()
        
        shapes = {'I': i_tet}

        return shapes[block]


    def receive_signal(self):

        while True:

            commands = {'p' : game.grid.draw_board, 
                        'g' : game.grid.given, 
                        'c' : game.grid.clear,
                        '?s': game.grid.show_score,
                        '?n': game.grid.show_clear_lines,
                        's' : game.grid.step,
                        't' : game.active_tet.print_tet}

            command =  raw_input()
   
            if command == 'q':
                break

            if command.isupper():
                self.active_tet = self.set_active_set(command)
            else:
                commands[command]()



if __name__ == '__main__':
    
    game = Operator()
    game.receive_signal()