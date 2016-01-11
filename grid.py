#!/usr/bin/env python

class Grid(object):

    def __init__(self):
        self.board = [[None] * 10 for i in range(22)]
        self.score = 0
        self.lines_clear = 0

    def draw_board(self):

        current_board = self.board
        
        for row in current_board:
            row = [cell or '.' for cell in row]
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
                del self.board[index]
                self.board.insert(0, [None]*10)
                self.score += 100
                self.lines_clear += 1
 