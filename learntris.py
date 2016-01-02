#!/usr/bin/env python


def draw_board():
    for row in range(0, 22):
        print '. '*10 

def main():
    
    command = raw_input()
    
    if command != 'q':
        draw_board()







if __name__ == '__main__':
    main()