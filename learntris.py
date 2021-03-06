#!/usr/bin/env python
"""Operator class to receive signals and control the game play"""
import sys

from game import Game

class Operator(object):
    """Handles receiving, parsing, and triaging incoming signals"""

    @classmethod
    def display(cls):
        """Cements any existing tetraminos to the board and prints state of board"""
        game.set_board('lower')
        game.grid.draw_board()

    @classmethod
    def spawn(cls):
        """Place a new tetramino on the board"""
        game.set_board('upper')
        game.grid.draw_board()

    @classmethod
    def new_line(cls):
        """prints new line"""
        print

    def signal_parser(self, signal):
        """Parses signals received from receive_signal()"""
        if signal == '?s' or signal == '?n':
            signals = [signal]

        else:
            signals = [s for s in signal if s != ' ']

        for sig in signals:
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
                        '<' : game.move_tet_west,
                        '>' : game.move_tet_east,
                        'v' : game.move_tet_south,
                        'V' : game.hard_drop}

            if sig.isupper() and not (sig == 'V' or sig == 'P'):
                game.active_tet = game.set_active_tet(sig)
            else:
                commands[sig]()


    def receive_signal(self):
        """receive commands from standard input"""
        while True:
            received = raw_input()
            self.signal_parser(received)

if __name__ == '__main__':
    game = Game()
    learntris = Operator()
    learntris.receive_signal()
