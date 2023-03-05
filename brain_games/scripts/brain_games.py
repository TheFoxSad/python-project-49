#!/usr/bin/env python3
import sys
from brain_games import logic
from brain_games.games import calc, even, prime, gcd, progression


my_dict = {"brain-calc"        : calc,
           "brain_even"        : even,
           "brain_prime"       : prime,
           "brain_gcd"         : gcd,
           "brain_progression" : progression}

def choice():
    game_name = sys.argv[0]
    value = my_dict.get(game_name)
    return value


def main():
    game = choice()
    logic.start_game(game)


if __name__ == '__main__':
    main()
