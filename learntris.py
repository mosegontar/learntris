#!/usr/bin/env python

import sys

from game import Game


class Operator(object):

    def display(self):

        game.set_board('lower')

        game.grid.draw_board()

    def spawn(self):

        game.set_board('upper')

        game.grid.draw_board()

    def new_line(self):
        print

    def signal_parser(self, signal):
        
        if signal == '?s' or signal == '?n':
            signals = [signal]

        else:
            signals = [s for s in signal if s != ' ']

        for s in signals:

            commands = {'p' : self.display,
                        'q' : sys.exit, 
                        'g' : game.grid.given, 
                        'c' : game.grid.clear,
                        '?s': game.grid.show_score,
                        '?n': game.grid.show_clear_lines,
                        's' : game.grid.step,
                        't' : game.active_tet.print_tet,
                        ')' : game.active_tet.rotate_clockwise,
                        '(' : game.active_tet.rotate_counter_clockwise,
                        ';' : self.new_line,
                        'P' : self.spawn,
                        '<' : game.active_tet.move_tet_west,
                        '>' : game.active_tet.move_tet_east,
                        'v' : game.active_tet.move_tet_south,
                        'V' : game.active_tet.hard_drop}

            if s.isupper() and not (s == 'V' or s == 'P'):
                game.active_tet = game.set_active_tet(s)
            else:
                commands[s]()


    def receive_signal(self):

        a = "cT vvvv vvvv vvvv vvvv vvvv vvvv Pq"
        b = "TVpq"
        c = "T)V pq"
        d = "cL >>>> ( >> <>>>< ( > )>>< vvpq"
        e = "cT <<< Pq"
        f = "TV Zv Pq"
        g = "c O P q"
        
        while True:

            received = raw_input()

            self.signal_parser(received)
        


if __name__ == '__main__':
    game = Game()
    main = Operator()
    main.receive_signal()