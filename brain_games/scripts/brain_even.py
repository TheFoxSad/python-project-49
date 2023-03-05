#!/usr/bin/env python3
import sys
from brain_games import logic
from brain_games.games import calc, even, prime, gcd, progression


my_dict = {"brain-calc"        : calc,
           "brain-prime"       : prime,
           "brain-gcd"         : gcd,
           "brain-progression" : progression,
           "brain-even"        : even}


def main():
    value = my_dict.get(sys.argv[0])
    logic.start_game(value)

if __name__ == '__main__':
    main()
