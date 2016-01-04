#!/usr/bin/env python

import sys

class Grid(object):

    def __init__(self):
        self.board = ['. '*10 for row in range(0,22)]
        self.score = 0
        self.lines_clear = 0

    def draw_board(self):

        for cell in self.board:
            print cell

    def given(self):
        self.board = []
        for row in range(0,22):
            self.board.append(raw_input())

    def clear(self):
        self.board = ['. '*10 for row in range(0,22)]

    def show_score(self):
        print self.score

    def show_clear_lines(self):
        print self.lines_clear

def main():
    
    grid = Grid()

    commands = {'p': grid.draw_board, 
                'g': grid.given, 
                'c': grid.clear,
                '?s': grid.show_score,
                '?n': grid.show_clear_lines}

    while True:
        command = raw_input()
        if command == 'q':
            break
        commands[command]()


if __name__ == '__main__':
    main()