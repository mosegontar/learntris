#!/usr/bin/env python

import sys

class Grid(object):

    def __init__(self):
        pass


def quit():
    pass

def draw_board():
    for row in range(0, 22):
        print '. '*10 
    #print "DRAWING"

def given():
    
    for ticker in range(0, 22):
        print raw_input()

def main():
    
    grid = Grid()

    commands = {'g':quit, 'p':draw_board, 'g':given, 'c':draw_board}
    
    command = raw_input()
    commands[command]()





if __name__ == '__main__':
    main()